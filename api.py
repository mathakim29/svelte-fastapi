from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Svelte FastAPI Template")

@app.get("/api/health")
def health():
    return {"message": "FastAPI is running"}

def main():
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
