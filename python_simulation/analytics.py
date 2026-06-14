import pandas as pd


class Analytics:

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def load(self):
        return pd.read_csv(self.csv_file)

    def average_voltage(self):
        df = self.load()
        return round(df["voltage"].mean(), 2)

    def average_current(self):
        df = self.load()
        return round(df["current"].mean(), 2)

    def average_power(self):
        df = self.load()
        return round(df["power"].mean(), 2)

    def peak_power(self):
        df = self.load()
        return round(df["power"].max(), 2)

    def total_cost(self):
        df = self.load()
        return round(df["cost"].max(), 2)