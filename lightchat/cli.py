# cli.py

import typer
from .trainer import Trainer
from .manager import ModelManager
from transformers import pipeline
import os

app = typer.Typer()

@app.command()
def train(
    model_name: str,
    file_path: str,
    epochs: int = 3,
    batch_size: int = 8,
    learning_rate: float = 5e-5,
    top_k: int = 50,
    top_p: float = 0.9
):
    """
    Train a new model and save to models/<model_name>. 
    """
    trainer = Trainer(model_name, file_path, epochs, batch_size, learning_rate)
    trainer.train()
    typer.echo(f"Model '{model_name}' trained and saved.")

@app.command()
def list_models():
    manager = ModelManager()
    models = manager.list_models()
    typer.echo("Available models:")
    for m in models:
        typer.echo(f"- {m}")

@app.command()
def delete_model(model_name: str):
    manager = ModelManager()
    manager.delete_model(model_name)
    typer.echo(f"Model '{model_name}' deleted.")

@app.command()
def chat(
    model_name: str,
    max_length: int = 100,
    top_k: int = 50,
    top_p: float = 0.9,
    temperature: float = 1.0
):
    """
    Chat with a saved model. Type exit/quit to stop.
    """
    path = os.path.join("models", model_name)
    if not os.path.isdir(path):
        typer.echo(f"[ERROR] '{model_name}' not found.")
        raise typer.Exit()

    typer.echo(f"[lightchat 🤖] Loaded {model_name}")
    gen = pipeline(
        "text-generation",
        model=path,
        do_sample=True,
        top_k=top_k,
        top_p=top_p,
        temperature=temperature
    )

    while True:
        text = input("User: ")
        if text.lower().strip() in ["exit","quit"]:
            print("Bot: Goodbye!")
            break
        out = gen(text, max_length=max_length)[0]["generated_text"]
        resp = out[len(text):].strip()
        print("Bot:", resp)
