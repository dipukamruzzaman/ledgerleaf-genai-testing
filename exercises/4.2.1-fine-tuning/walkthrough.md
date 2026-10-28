# HO-4.2.1 — Observe a fine-tuning process (walkthrough)

**Goal of the fine-tune:** teach a small model to turn a LedgerLeaf acceptance criterion into ONE Gherkin
scenario in our house style (tags @US-xx @ACx, business-level steps, exact messages) — without long few-shot prompts.

## Step 1 — Select the model
| Choice | Why |
|---|---|
| **SLM:** Llama 3.2 3B (you have it in Ollama) | Small enough to fine-tune on one free cloud GPU; fast and cheap to run afterwards |
| Method: **LoRA** (parameter-efficient fine-tuning) | Trains small adapter layers (~1% of weights) instead of the whole model → minutes, not days |
| Where: a free notebook GPU (e.g. Google Colab T4) | Fine-tuning needs a GPU; a 16 GB laptop CPU is too slow |

## Step 2 — The dataset (train.jsonl)
Each line = one example: `input` (an acceptance criterion) → `output` (the scenario we want).
A real dataset needs **hundreds** of reviewed examples; train.jsonl shows 6 of them.
**Your task:** two of the six examples are BAD training data. Find them (see notes.md).

## Step 3 — The fine-tuning code (Hugging Face TRL + PEFT — shown, not run)
```python
from datasets import load_dataset
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

data = load_dataset("json", data_files="train.jsonl")["train"].train_test_split(test_size=0.2)

def to_text(ex):                      # one training string per example
    return {"text": f"### Acceptance criterion:\n{ex['input']}\n### Gherkin:\n{ex['output']}"}
data = data.map(to_text)

trainer = SFTTrainer(
    model="meta-llama/Llama-3.2-3B-Instruct",
    train_dataset=data["train"],
    eval_dataset=data["test"],          # held-out examples to detect overfitting
    peft_config=LoraConfig(r=16, lora_alpha=32, target_modules="all-linear"),
    args=SFTConfig(output_dir="ledgerleaf-gherkin-lora", num_train_epochs=3,
                   learning_rate=2e-4, per_device_train_batch_size=4,
                   eval_strategy="epoch", logging_steps=10),
)
trainer.train()                        # watch train loss AND eval loss
trainer.save_model()                   # saves the small LoRA adapter (a few MB)
```
Key settings: **test split** (keeps unseen data for evaluation) · **epochs** (too many → overfitting) ·
**eval loss** (if train loss falls but eval loss rises → overfitting).

## Step 4 — Prompt the fine-tuned model and discuss the output
Prompt (no examples needed any more — the style is "baked in"):
```text
### Acceptance criterion:
US-05 AC2: Transfers are allowed up to $5,000.00 per transfer (inclusive).
### Gherkin:
```
Before looking at the answer: given train.jsonl as it is, what do you think the fine-tuned model will
output for this prompt? Write your guess in notes.md, then we discuss it.
