import requests
from dotenv import load_dotenv
import os

# Загрузи конфигурацию из .env
load_dotenv()
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Эндпоинт Ollama

def ask_ollama(question):
    data = {
        "model": "llama2",  # Укажи модель, которую ты установил
        "prompt": question,
        "stream": False,  # Отключи потоковый вывод для простоты
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=data)
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"