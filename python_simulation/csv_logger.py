import os

import pandas as pd

from config.settings import CSV_FILE


class CSVLogger:

    def __init__(self):

        self.file = CSV_FILE

        self.initialize_file()

    def initialize_file(self):

        if not os.path.exists(
            self.file
        ):

            columns = [

                "timestamp",

                "voltage",

                "current",

                "power",

                "energy",

                "cost",

                "load",

                "alert"
            ]

            pd.DataFrame(
                columns=columns
            ).to_csv(
                self.file,
                index=False
            )

    def log(
        self,
        row
    ):

        pd.DataFrame(
            [row]
        ).to_csv(

            self.file,

            mode="a",

            index=False,

            header=False
        )