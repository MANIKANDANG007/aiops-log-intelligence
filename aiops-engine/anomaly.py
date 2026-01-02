import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(error_counts):
    X = np.array(error_counts).reshape(-1, 1)
    model = IsolationForest(contamination=0.15, random_state=42)
    preds = model.fit_predict(X)
    return preds
