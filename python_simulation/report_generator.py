import pandas as pd


class ReportGenerator:

    def __init__(
        self,
        file_path
    ):

        self.file_path = file_path

    def load_data(self):

        return pd.read_csv(
            self.file_path
        )

    def summary(self):

        df = self.load_data()

        return {

            "records":
            len(df),

            "max_power":
            df["power"].max(),

            "avg_power":
            round(
                df["power"].mean(),
                2
            ),

            "total_energy":
            round(
                df["energy"].max(),
                4
            ),

            "total_cost":
            round(
                df["cost"].max(),
                2
            )
        }