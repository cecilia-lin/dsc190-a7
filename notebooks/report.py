import marimo

__generated_with = "0.23.5"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("../data/features/events.csv")
    
    df
    return (df,)


@app.cell
def _(df, plt):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df["duration_minutes"].dropna(), bins=30, edgecolor="black", color="skyblue")

    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (Minutes)")
    ax.set_ylabel("Frequency")

    # Display the figure in Marimo
    fig
    return


if __name__ == "__main__":
    app.run()
