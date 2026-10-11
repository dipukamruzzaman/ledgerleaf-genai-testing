"""Smoke tests: prove the app is running. Real tests are built during the exercises."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "app"))
import app as bank  # noqa: E402

import pytest


@pytest.fixture
def client():
    bank._seed()
    bank.app.config["TESTING"] = True
    with bank.app.test_client() as c:
        yield c


def test_home_redirects_to_login(client):
    r = client.get("/")
    assert r.status_code == 302 and "/login" in r.headers["Location"]


def test_demo_user_can_log_in(client):
    r = client.post("/api/login", json={"email": "alex.tester@ledgerleaf.test", "password": "Passw0rd!"})
    assert r.status_code == 200 and r.get_json()["name"] == "Alex Tester"


def test_accounts_are_listed(client):
    r = client.get("/api/accounts/alex.tester@ledgerleaf.test")
    assert [a["number"] for a in r.get_json()] == ["100-001", "100-002"]


def test_simple_transfer(client):
    r = client.post("/api/transfers", json={"email": "alex.tester@ledgerleaf.test",
                    "from_account": "100-001", "to_account": "100-002", "amount": "100.00"})
    assert r.status_code == 201
