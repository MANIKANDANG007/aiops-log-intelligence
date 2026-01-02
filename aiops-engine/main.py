from anomaly import detect_anomalies

# demo error counts per minute (simulate spikes)
error_counts = [1, 2, 1, 2, 1, 40, 2, 1]

preds = detect_anomalies(error_counts)

for i, p in enumerate(preds):
    if p == -1:
        print(f"Anomaly detected at minute {i} (count={error_counts[i]})")
