import gradio as gr
import requests

def chat(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt}
    )
    return response.json()["response"]

gr.ChatInterface(chat).launch()
