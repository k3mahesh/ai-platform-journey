import os, time, httpx
from dotenv import load_dotenv

load_dotenv()  # reads the .env file

PROMPT = "Explain a Kubernetes pod in one sentence."

# 1. Local model (Ollama, on your Mac)
t = time.time()
r = httpx.post("http://localhost:11434/api/generate", timeout=120,
               json={"model": "llama3.2:3b", "prompt": PROMPT, "stream": False})
d = r.json()
print("LOCAL :", d["response"].strip())
print(f"        tokens in={d['prompt_eval_count']} out={d['eval_count']}  time={time.time()-t:.1f}s\n")

# 2. Hosted model (Gemini, on Google's servers)
model = os.environ["GEMINI_MODEL"]
t = time.time()
r = httpx.post(
    f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
    headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"]},
    json={"contents": [{"parts": [{"text": PROMPT}]}]}, timeout=60)
r.raise_for_status()
d = r.json()
u = d["usageMetadata"]
print("HOSTED:", d["candidates"][0]["content"]["parts"][0]["text"].strip())
print(f"        tokens in={u['promptTokenCount']} out={u.get('candidatesTokenCount')}  time={time.time()-t:.1f}s")
