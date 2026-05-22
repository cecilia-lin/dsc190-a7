import pandas as pd
import os

# Update if your assignment specifies different valid events
VALID_EVENTS = ['click', 'view', 'purchase', 'login'] 

def main():
    os.makedirs('data/clean', exist_ok=True)
    df = pd.read_csv('data/raw/events.csv')

    # 1. Drop rows with any missing fields
    df = df.dropna()

    # 2. Convert to lowercase and filter out invalid event_types
    df['event_type'] = df['event_type'].str.lower()
    df = df[df['event_type'].isin(VALID_EVENTS)]

    # 3. Drop non-positive duration_seconds
    df = df[df['duration_seconds'] > 0]

    # 4. Normalize timestamp to ISO 8601 (YYYY-MM-DDTHH:MM:SS)
    # Added format='mixed' to handle the raw data format safely
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed').dt.strftime('%Y-%m-%dT%H:%M:%S')

    df.to_csv('data/clean/events.csv', index=False)

if __name__ == '__main__':
    main()