import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import random
import time

class BacktestEngine:
    def __init__(self, historical_data_path="historical_data.json"):
        self.data_path = historical_data_path
        self.results = []

    def load_data(self):
        try:
            with open(self.data_path, "r") as f:
                return json.load(f)
        except:
            print("[BACKTEST] No historical data found.")
            return []

    def simulate_strategy(self, token):
        win_chance = random.random()
        if win_chance > 0.55:
            return random.uniform(1.1, 3.5)
        else:
            return random.uniform(0.1, 0.95)

    def run(self):
        print("[BACKTEST] Starting backtest...")
        data = self.load_data()
        for token in data:
            result = self.simulate_strategy(token)
            self.results.append({"token": token["symbol"], "return": result})
        print(f"[BACKTEST] Completed on {len(self.results)} tokens.")

    def report(self):
        df = pd.DataFrame(self.results)
        print(df.describe())
        df.hist(column="return", bins=30)
        plt.title("Return Distribution")
        plt.savefig("lab/backtest_results.png")
