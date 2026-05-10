# Veridion Canary

Small sample service repo used to validate Veridion as an external install.

## Smoke Scenario

This branch is a docs-only change used to validate a low-risk GO decision.

## Service

- Python API surface
- dependency manifest
- Docker image
- Kubernetes deployment
- Terraform service and IAM resources
- database migration placeholder

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
```
