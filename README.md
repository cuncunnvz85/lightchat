# LightChat

![Downloads](https://static.pepy.tech/badge/lightchat/month)  

LightChat is a lightweight GPT-2–based toolkit built on top of DistilGPT2. It enables anyone to train, deploy, and interact with a custom chatbot on low‑end devices using simple CLI commands.


## 🌐 Links & Community

- 🔗 GitHub Repository: [github.com/reprompts/lightchat](https://github.com/reprompts/lightchat)
- 💼 LinkedIn Group: [LightChat Dev Group](https://www.linkedin.com/groups/14631875/)
- 📰 Dev.to Profile: [@repromptsquest](https://dev.to/repromptsquest)
- 🐦 Twitter: [@repromptsquest](https://twitter.com/repromptsquest)



---

## 🔧 Features

* **Train** your own language model on plain text files
* **Chat** interactively with your fine‑tuned model
* **List** & **delete** saved models
* Supports **top‑k** and **top‑p** (nucleus) sampling

---

## 📋 Dataset Preparation

* Provide a **plain text** file (`.txt`) with **one sentence per line**.
* Aim for at least **1,000–10,000 lines** for reasonable results on CPU.
* Clean, focused content yields better chat relevance.

**Example** (`data.txt`):

```
Hello, how can I help you today?
I love reading sci‑fi novels.
What's the weather like?
```

---

## ⚙️ Installation

```bash
pip install lightchat
```

> **⚠️ CPU install note:** Transformers and PyTorch may take several minutes to compile on CPU.

---

## 🚀 Training

```bash
lightchat train <model_name> <data.txt> \
  --epochs 3 \
  --batch-size 8 \
  --learning-rate 5e-5

Example Command:
lightchat train newmodel data.txt --epochs 1 --batch-size 8 --learning-rate 5e-5


> **⚠️ Data file path <data.txt>:** Give proper path to the dataset or keep dataset inside the root directory of project where library is installed.

```

* **model\_name**: directory under `models/` to save to
* **epochs**: full passes over your data
* **batch-size**: number of samples per step
* **learning-rate**: step size for optimizer

> **⚠️ CPU training note:** Training on CPU is slow. More epochs/bigger batch sizes = longer time but better fit.

---

## 💬 Chatting

```bash
lightchat chat <model_name> \
  --max-length 100 \
  --top-k 50 \
  --top-p 0.9 \
  --temperature 1.0


Example Command:
lightchat chat newmodel --max-length 100 --top-k 50 --temperature 0.9

```

* **max-length**: max generated tokens per reply
* **top-k**: sample from top *k* tokens
* **top-p**: sample from top cumulative probability *p*
* **temperature**: randomness control (higher = more creative)


Give "exit" as an prompt to the model to exit the conversation and you can load the trained models anytime by following the instructions given below. 


> Trained models live in `models/<model_name>/`.

---

## 📂 Model Management

* **List** saved models: `lightchat list-models`
* **Delete** a model: `lightchat delete-model <model_name>`
* Or manually remove `models/<model_name>/` directory.

---

## 🙌 Contributions

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md).
