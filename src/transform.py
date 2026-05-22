import pandas as pd
import os

def main():
    os.makedirs('data/transformed', exist_ok=True)
    df = pd.read_csv('data/clean/events.csv')

    # Add date column (YYYY-MM-DD)
    df['date'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')

    df.to_csv('data/transformed/events.csv', index=False)

if __name__ == '__main__':
    main()