# trainer.py

import os
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer as HFTrainer,
    TrainingArguments,
    DataCollatorForLanguageModeling,
)
from datasets import load_dataset

class Trainer:
    def __init__(self, model_name, file_path, epochs=3, batch_size=8, learning_rate=5e-5):
        self.model_name = model_name
        self.file_path = file_path
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.output_dir = os.path.join("models", model_name)

    def train(self):
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained("distilgpt2", use_fast=True)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "right"

        model = AutoModelForCausalLM.from_pretrained("distilgpt2")

        # Load and tokenize dataset
        dataset = load_dataset('text', data_files={'train': self.file_path})
        tokenized = dataset.map(
            lambda x: tokenizer(
                x['text'], padding=True, truncation=True, max_length=512
            ),
            batched=True,
        )

        # Training arguments
        training_args = TrainingArguments(
            output_dir=self.output_dir,
            overwrite_output_dir=True,
            num_train_epochs=self.epochs,
            per_device_train_batch_size=self.batch_size,
            learning_rate=self.learning_rate,
            logging_dir=os.path.join(self.output_dir, "logs"),
            save_total_limit=2,
            save_steps=500,
            logging_steps=100,
            fp16=True,
            report_to="none"
        )

        # Initialize and run HF Trainer
        trainer = HFTrainer(
            model=model,
            args=training_args,
            train_dataset=tokenized['train'],
            tokenizer=tokenizer,
            data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
        )
        trainer.train()

        # Save
        model.save_pretrained(self.output_dir)
        tokenizer.save_pretrained(self.output_dir)
