from fastapi import FastAPI
import subprocess


app = FastAPI(title="veridion-canary")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/payments/config")
def payment_config() -> dict[str, object]:
    return {
        "service": "payments-api",
        "region": "us-central1",
        "rollout": "canary",
        "public": True,
    }


@app.post("/admin/reload")
def reload_config(environment: str) -> dict[str, object]:
    subprocess.run(f"echo reloading {environment}", shell=True, check=False)
    return {"reloaded": True, "environment": environment}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
