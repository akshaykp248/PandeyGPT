from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "mistralai/Mistral-7B-v0.1"
HF_TOKEN = os.getenv("HF_TOKEN")

class LLMModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=HF_TOKEN)
        self.model = None  # Lazy load the model for faster start-up

    def load_model(self):
        if self.model is None:
            self.model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, use_auth_token=HF_TOKEN)

    def generate_text(self, prompt, max_length=200):
        self.load_model()  # Load the model only when required
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs, skip_special_tokens=True)

model = LLMModel()
