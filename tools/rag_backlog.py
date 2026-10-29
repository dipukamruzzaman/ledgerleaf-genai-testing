"""
HO-4.1.2 - Experiment with Retrieval-Augmented Generation (RAG) for a test task (LedgerLeaf Bank)

"Ask the requirements": index docs/requirements/*.md, retrieve the most similar chunks for a question,
and let the LLM answer ONLY from those chunks. Everything runs locally with Ollama.

    python tools/rag_backlog.py                      # chunk = one section per "## " heading, top-k 3
    python tools/rag_backlog.py --chunk-size 200     # fixed-size chunks of ~200 characters instead
    python tools/rag_backlog.py --top-k 1            # retrieve only the single best chunk
    python tools/rag_backlog.py --question "How many payees can a customer have?"

Without --question it runs the 6 questions from QUESTIONS below and writes a report to reports/.
"""
import argparse
import glob
import math
import pathlib
import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
QUESTIONS = [
    "What is the maximum amount a customer can transfer?",
    "At what age can a customer open an account?",
    "After how many failed log-in attempts is an account locked?",
    "How many payees can a customer have?",
    "What fee is charged for a transfer?",
    "How long is a password reset link valid?",
]


# ------------------------------------------------------------------ 1. chunking
def load_chunks(chunk_size=None):
    chunks = []
    for path in sorted(glob.glob(str(ROOT / "docs" / "requirements" / "*.md"))):
        name = pathlib.Path(path).name
        text = pathlib.Path(path).read_text(encoding="utf-8")
        if chunk_size:                                   # fixed-size chunks (may cut sentences)
            parts = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        else:                                            # one chunk per "## " section
            parts, current = [], []
            for line in text.splitlines():
                if line.startswith("## ") and current:
                    parts.append("\n".join(current)); current = []
                current.append(line)
            parts.append("\n".join(current))
        chunks += [{"source": f"{name}#{i + 1}", "text": p.strip()} for i, p in enumerate(parts) if p.strip()]
    return chunks


# ------------------------------------------------------------------ 2. embeddings + retrieval
def embed(texts):
    r = requests.post(f"{OLLAMA}/api/embed", json={"model": EMBED_MODEL, "input": texts}, timeout=300)
    r.raise_for_status()
    return r.json()["embeddings"]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def retrieve(question, chunks, vectors, k, embed_fn=embed):
    q = embed_fn(["search_query: " + question])[0]
    scored = sorted(((cosine(q, v), c) for v, c in zip(vectors, chunks)), key=lambda t: t[0], reverse=True)
    return scored[:k]


# ------------------------------------------------------------------ 3. generation
PROMPT = """You answer questions about the LedgerLeaf Bank requirements.
Use ONLY the context below. Cite the source in brackets, e.g. [user-stories.md#6].
If the context does not contain the answer, reply exactly: NOT FOUND IN THE DOCUMENTS.

CONTEXT:
{context}

QUESTION: {question}
ANSWER:"""


def generate(model, question, hits):
    context = "\n\n".join(f"[{c['source']}]\n{c['text']}" for _, c in hits)
    r = requests.post(f"{OLLAMA}/api/generate", json={
        "model": model, "prompt": PROMPT.format(context=context, question=question),
        "stream": False, "options": {"temperature": 0}}, timeout=600)
    r.raise_for_status()
    return r.json()["response"].strip()


def main(embed_fn=embed, generate_fn=generate):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="llama3.1:8b")
    ap.add_argument("--chunk-size", type=int, default=None, help="fixed chunk size in characters")
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--question", default=None)
    a = ap.parse_args()

    chunks = load_chunks(a.chunk_size)
    print(f"Indexed {len(chunks)} chunks from docs/requirements/ "
          f"({'fixed ' + str(a.chunk_size) + ' chars' if a.chunk_size else 'one per ## section'}).")
    vectors = embed_fn(["search_document: " + c["text"] for c in chunks])

    questions = [a.question] if a.question else QUESTIONS
    tag = f"chunk{a.chunk_size or 'section'}_top{a.top_k}"
    md = [f"# HO-4.1.2 RAG run — {a.model}, {tag}", ""]
    for i, q in enumerate(questions, 1):
        hits = retrieve(q, chunks, vectors, a.top_k, embed_fn)
        answer = generate_fn(a.model, q, hits)
        print(f"\nQ{i}: {q}")
        for score, c in hits:
            print(f"   retrieved {c['source']:<32} score {score:.3f}  | {c['text'][:60].replace(chr(10), ' ')}…")
        print(f"   ANSWER: {answer}")
        md += [f"## Q{i}: {q}", "Retrieved: " + ", ".join(f"{c['source']} ({s:.3f})" for s, c in hits), "",
               f"**Answer:** {answer}", ""]
    if not a.question:
        out = ROOT / "reports" / f"4.1.2-rag_{tag}.md"
        out.parent.mkdir(exist_ok=True)
        out.write_text("\n".join(md) + "\n", encoding="utf-8")
        print(f"\nReport written to {out}")


if __name__ == "__main__":
    main()
