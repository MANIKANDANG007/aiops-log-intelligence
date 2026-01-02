def summarize(errors):
    # simple placeholder for log clustering
    return {
        "service": "payment",
        "probable_cause": max(errors, key=errors.count) if errors else "unknown"
    }
