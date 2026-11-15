import os, time, httpx
from dotenv import load_dotenv

load_dotenv()  # reads the .env file

PROMPT = "Explain a Kubernetes pod in one sentence."

# Local model (Ollama, on your Mac)
host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
model = os.environ.get("OLLAMA_MODEL", "llama3.2:3b")
t = time.time()
r = httpx.post(f"{host}/api/generate", timeout=120,
               json={"model": model, "prompt": PROMPT, "stream": False})
r.raise_for_status()
d = r.json()
print("LOCAL :", d["response"].strip())
print(f"        tokens in={d['prompt_eval_count']} out={d['eval_count']}  time={time.time()-t:.1f}s")
