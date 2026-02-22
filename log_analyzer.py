import docker
import requests
import json
import time

# Configuration for Docker Model Runner (Standard Port 8000)
AI_URL = "http://localhost:8000/v1/chat/completions"
MODEL = "llama.cpp" # Your status showed llama.cpp backend active

def analyze_with_ai(log_text):
    """Sends log text to the local Docker Model Runner."""
    prompt = f"You are a Senior SRE. Analyze this Docker log, explain the cause, and provide a 1-line fix command:\n\n{log_text}"
    
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(AI_URL, json=payload, timeout=30)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error connecting to AI: {e}"

def monitor_containers():
    client = docker.from_env()
    print("🚀 Starting AI Log Monitor (Local SmolLM2)...")
    
    # Monitor all running containers
    for container in client.containers.list():
        print(f"📦 Monitoring: {container.name}")
        
        # Get last 5 lines of logs
        logs = container.logs(tail=5).decode('utf-8').strip()
        
        if "error" in logs.lower() or "fail" in logs.lower() or "exception" in logs.lower():
            print(f"⚠️ Issue detected in {container.name}!")
            analysis = analyze_with_ai(logs)
            print(f"🤖 AI Analysis:\n{analysis}\n" + "-"*50)
        else:
            print(f"✅ {container.name} logs look healthy.")

if __name__ == "__main__":
    monitor_containers()