"""
LedgerLeaf Bank - a small, fictional online-banking app used as the
system under test for the "GenAI-Assisted Testing" project.

It is deliberately simple (in-memory data, no real email) so that every
exercise is repeatable. It is NOT production code.

Run:  python app/app.py      then open http://127.0.0.1:5000
"""
from datetime import datetime, timedelta, date
from decimal import Decimal, InvalidOperation
import re
import secrets

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "ledgerleaf-demo-only"

MAX_TRANSFER = Decimal("5000.00")          # per-transfer limit (see user stories)
MAX_FAILED_LOGINS = 3                      # lock account after this many failures
PASSWORD_RULE = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$")
EMAIL_RULE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

USERS = {}      # email -> user dict
ACCOUNTS = {}   # account number -> account dict
OUTBOX = []     # simulated e-mails
RESET_TOKENS = {}  # token -> {"email":..., "created":...}
TRANSFERS = []


def _seed():
    USERS.clear(); ACCOUNTS.clear(); OUTBOX.clear(); RESET_TOKENS.clear(); TRANSFERS.clear()
    _create_user("alex.tester@ledgerleaf.test", "Passw0rd!", "Alex Tester", "1990-04-12")
    _create_user("sam.saver@ledgerleaf.test", "Savings123", "Sam Saver", "1985-11-02")
    ACCOUNTS["100-001"]["balance"] = Decimal("12500.00")
    ACCOUNTS["100-002"]["balance"] = Decimal("800.00")


def _create_user(email, password, name, dob):
    n = len(USERS) + 1
    chequing, savings = f"100-{2*n-1:03d}", f"100-{2*n:03d}"
    USERS[email] = {"email": email, "password": password, "name": name, "dob": dob,
                    "failed": 0, "locked": False, "accounts": [chequing, savings]}
    ACCOUNTS[chequing] = {"number": chequing, "type": "Chequing", "owner": email, "balance": Decimal("0.00")}
    ACCOUNTS[savings] = {"number": savings, "type": "Savings", "owner": email, "balance": Decimal("0.00")}
    return USERS[email]


def _age(dob_text):
    born = datetime.strptime(dob_text, "%Y-%m-%d").date()
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# ---------------------------------------------------------------- business logic
def register(email, password, name, dob):
    errors = []
    if not EMAIL_RULE.match(email or ""):
        errors.append("Enter a valid email address.")
    elif email in USERS:
        errors.append("An account with this email already exists.")
    if not PASSWORD_RULE.match(password or ""):
        errors.append("Password must be at least 8 characters and include upper case, lower case and a number.")
    if not name or not name.strip():
        errors.append("Enter your full name.")
    try:
        if _age(dob) < 17:
            errors.append("You must be at least 18 years old to open an account.")
    except (TypeError, ValueError):
        errors.append("Enter your date of birth as YYYY-MM-DD.")
    if errors:
        return None, errors
    return _create_user(email, password, name.strip(), dob), []


def login(email, password):
    user = USERS.get(email)
    if not user:
        return None, "Invalid email or password."
    if user["locked"]:
        return None, "Your account is locked. Reset your password to unlock it."
    if user["password"] != password:
        user["failed"] += 1
        if user["failed"] > MAX_FAILED_LOGINS:
            user["locked"] = True
            return None, "Your account is locked. Reset your password to unlock it."
        return None, "Invalid email or password."
    user["failed"] = 0
    return user, None


def request_reset(email):
    # Always the same message, so the page does not reveal which emails exist.
    if email in USERS:
        token = secrets.token_urlsafe(16)
        RESET_TOKENS[token] = {"email": email, "created": datetime.now()}
        OUTBOX.append({"to": email, "subject": "Reset your LedgerLeaf password",
                       "link": f"/reset/{token}", "sent": datetime.now().isoformat(timespec="seconds")})
    return "If an account exists for this email, a reset link has been sent."


def complete_reset(token, new_password):
    entry = RESET_TOKENS.get(token)
    if not entry:
        return False, "This reset link is invalid."
    if not PASSWORD_RULE.match(new_password or ""):
        return False, "Password must be at least 8 characters and include upper case, lower case and a number."
    user = USERS[entry["email"]]
    user.update(password=new_password, failed=0, locked=False)
    del RESET_TOKENS[token]
    return True, "Your password has been changed. You can now log in."


def transfer(email, from_acc, to_acc, amount_text, memo=""):
    try:
        amount = Decimal(str(amount_text)).quantize(Decimal("0.01"))
    except (InvalidOperation, TypeError):
        return None, "Enter a valid amount."
    src, dst = ACCOUNTS.get(from_acc), ACCOUNTS.get(to_acc)
    if not src or src["owner"] != email:
        return None, "Choose one of your own accounts to transfer from."
    if not dst:
        return None, "The destination account does not exist."
    if from_acc == to_acc:
        return None, "Choose two different accounts."
    if amount >= MAX_TRANSFER:
        return None, f"The maximum per transfer is ${MAX_TRANSFER:,.2f}."
    if amount > src["balance"]:
        return None, "Insufficient funds."
    src["balance"] -= amount
    dst["balance"] += amount
    rec = {"id": len(TRANSFERS) + 1, "from": from_acc, "to": to_acc, "amount": str(amount),
           "memo": memo[:140], "at": datetime.now().isoformat(timespec="seconds")}
    TRANSFERS.append(rec)
    return rec, None


# ---------------------------------------------------------------- web pages
def current_user():
    return USERS.get(session.get("email"))


@app.route("/")
def home():
    return redirect(url_for("dashboard") if current_user() else url_for("login_page"))


@app.route("/login", methods=["GET", "POST"])
def login_page():
    error = None
    if request.method == "POST":
        user, error = login(request.form.get("email", "").strip(), request.form.get("password", ""))
        if user:
            session["email"] = user["email"]
            return redirect(url_for("dashboard"))
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))


@app.route("/register", methods=["GET", "POST"])
def register_page():
    errors = []
    if request.method == "POST":
        f = request.form
        user, errors = register(f.get("email", "").strip(), f.get("password", ""), f.get("name", ""), f.get("dob", ""))
        if user:
            return render_template("message.html", title="Welcome to LedgerLeaf",
                                   message="Your account has been created. You can now log in.")
    return render_template("register.html", errors=errors)


@app.route("/forgot", methods=["GET", "POST"])
def forgot_page():
    message = None
    if request.method == "POST":
        message = request_reset(request.form.get("email", "").strip())
    return render_template("forgot.html", message=message)


@app.route("/reset/<token>", methods=["GET", "POST"])
def reset_page(token):
    error = message = None
    if request.method == "POST":
        ok, text = complete_reset(token, request.form.get("password", ""))
        if ok:
            return render_template("message.html", title="Password changed", message=text)
        error = text
    return render_template("reset.html", error=error, message=message)


@app.route("/dashboard")
def dashboard():
    user = current_user()
    if not user:
        return redirect(url_for("login_page"))
    accounts = [ACCOUNTS[a] for a in user["accounts"]]
    return render_template("dashboard.html", user=user, accounts=accounts)


@app.route("/transfer", methods=["GET", "POST"])
def transfer_page():
    user = current_user()
    if not user:
        return redirect(url_for("login_page"))
    error = done = None
    if request.method == "POST":
        f = request.form
        done, error = transfer(user["email"], f.get("from_account"), f.get("to_account"), f.get("amount"), f.get("memo", ""))
    accounts = [ACCOUNTS[a] for a in user["accounts"]]
    return render_template("transfer.html", accounts=accounts, error=error, done=done, limit=MAX_TRANSFER)


@app.route("/outbox")
def outbox_page():
    """Simulated mailbox so testers can see password-reset e-mails."""
    return render_template("outbox.html", mails=list(reversed(OUTBOX)))


# ---------------------------------------------------------------- JSON API
@app.post("/api/login")
def api_login():
    d = request.get_json(silent=True) or {}
    user, error = login(d.get("email", ""), d.get("password", ""))
    if not user:
        return jsonify(error=error), 401
    return jsonify(email=user["email"], name=user["name"])


@app.post("/api/register")
def api_register():
    d = request.get_json(silent=True) or {}
    user, errors = register(d.get("email", ""), d.get("password", ""), d.get("name", ""), d.get("dob", ""))
    if not user:
        return jsonify(errors=errors), 400
    return jsonify(email=user["email"], accounts=user["accounts"]), 201


@app.get("/api/accounts/<email>")
def api_accounts(email):
    user = USERS.get(email)
    if not user:
        return jsonify(error="Not found"), 404
    return jsonify([{**ACCOUNTS[a], "balance": str(ACCOUNTS[a]["balance"])} for a in user["accounts"]])


@app.post("/api/transfers")
def api_transfer():
    d = request.get_json(silent=True) or {}
    rec, error = transfer(d.get("email", ""), d.get("from_account"), d.get("to_account"), d.get("amount"), d.get("memo", ""))
    if error:
        return jsonify(error=error), 400
    return jsonify(rec), 201


@app.post("/api/password-reset")
def api_reset_request():
    d = request.get_json(silent=True) or {}
    return jsonify(message=request_reset(d.get("email", "")))


@app.get("/api/outbox")
def api_outbox():
    return jsonify(OUTBOX)


@app.post("/api/test/reset")
def api_test_reset():
    """Test hook: restore the seeded demo data."""
    _seed()
    return jsonify(status="reset")


_seed()

if __name__ == "__main__":
    app.run(debug=True)
