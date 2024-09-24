"""Plot our raw data."""

import os

import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/raw/data.csv").set_index("time")
    ax = df.voltage.plot()
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/voltage-time-series.png")
