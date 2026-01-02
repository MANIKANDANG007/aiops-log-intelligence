# AIOps Log Intelligence Platform

Log-driven AIOps system to reduce alert noise in production using ML-based anomaly detection.

## Architecture
Application Logs → Promtail → Loki → AIOps Engine → Intelligent Alerts

## Features
- ML-based anomaly detection (Isolation Forest)
- Log-first approach for better signal
- Reduced alert noise and faster triage

## How to Run
1. docker-compose up
2. python aiops-engine/main.py

## Future Work
- Streaming ingestion
- Feedback loop for retraining
- Alertmanager integration
