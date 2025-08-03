# app/utils/data_utils.py
import pandas as pd
import os

DATA_PATH = "app/data/learning_log.csv"

def save_entry(date, topic, duration, notes):
    os.makedirs("app/data", exist_ok=True)
    entry = pd.DataFrame([{
        "date": pd.to_datetime(date),
        "topic": topic,
        "duration": duration,
        "notes": notes
    }])
    
    if os.path.exists(DATA_PATH):
        existing = pd.read_csv(DATA_PATH, parse_dates=["date"])
        updated = pd.concat([existing, entry], ignore_index=True)
        updated.to_csv(DATA_PATH, index=False)
    else:
        entry.to_csv(DATA_PATH, index=False)

def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH, parse_dates=["date"])
    else:
        return pd.DataFrame(columns=["date", "topic", "duration", "notes"])
