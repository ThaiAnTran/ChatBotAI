# ollama_interface.py
import requests
import config

def get_response(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": config.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi kết nối với Ollama: {e}")
        return "Xin lỗi, tôi không thể trả lời lúc này."