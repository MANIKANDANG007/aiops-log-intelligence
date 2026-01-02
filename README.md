# AIOps Log Intelligence Platform

Log-driven AIOps system designed to reduce alert noise in production environments
using ML-based anomaly detection.

## Architecture
Application Logs → Promtail → Loki → AIOps Engine → Intelligent Alerts

## Features
- Log-based anomaly detection using Isolation Forest
- Reduced alert noise by focusing on abnormal patterns
- Faster triage with actionable incident insights
- Log-first approach for better signal quality

## Tech Stack
- Python
- Loki & Promtail
- Docker
- Machine Learning (Isolation Forest)

## How to Run
1. Start log pipeline:
   ```bash
   docker-compose up

