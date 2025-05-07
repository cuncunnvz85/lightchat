import os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from .config import MODELS_DIR

class ModelManager:
    def __init__(self):
        self.models_dir = MODELS_DIR

    def list_models(self):
        return [name for name in os.listdir(self.models_dir) if os.path.isdir(os.path.join(self.models_dir, name))]

    def load_model(self, model_name):
        model_path = os.path.join(self.models_dir, model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(model_path)
        return pipeline('text-generation', model=model, tokenizer=tokenizer)

    def delete_model(self, model_name):
        model_path = os.path.join(self.models_dir, model_name)
        if os.path.exists(model_path):
            import shutil
            shutil.rmtree(model_path)