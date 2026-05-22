import pandas as pd
import os

def main():
    os.makedirs('data/features', exist_ok=True)
    df = pd.read_csv('data/transformed/events.csv')

    # Add duration_minutes
    df['duration_minutes'] = df['duration_seconds'] / 60.0

    # Add weekday name written in full
    df['weekday'] = pd.to_datetime(df['date']).dt.day_name()

    df.to_csv('data/features/events.csv', index=False)

if __name__ == '__main__':
    main()