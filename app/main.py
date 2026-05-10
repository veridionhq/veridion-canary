from fastapi import FastAPI


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
