# AIOps Log Intelligence Platform

This project demonstrates a log-driven AIOps system designed to reduce alert
noise in production environments using machine learning.

## Architecture
Application Logs → Promtail → Loki → AIOps Engine → Intelligent Alerts

## Key Features
- Log-based anomaly detection using Isolation Forest
- Reduced alert noise by focusing on abnormal patterns
- Actionable incident summaries

## Tech Stack
- Python
- Loki & Promtail
- Docker
- Machine Learning (Isolation Forest)

## How to Run
1. docker-compose up
2. python aiops-engine/main.py

## Future Improvements
- Streaming-based processing
- Feedback loop for model retraining
- Integration with alert managers
# aiops-log-intelligence
Log-driven AIOps system to reduce alert noise in production using ML-based anomaly detection.
