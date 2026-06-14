import pandas as pd
import os
from datetime import datetime

CSV_FILE = "data/energy_log.csv"

def log_data(metrics):

    row = {
        "timestamp": datetime.now(),
        **metrics
    }

    df = pd.DataFrame([row])

    if not os.path.exists(CSV_FILE):
        df.to_csv(
            CSV_FILE,
            index=False
        )
    else:
        df.to_csv(
            CSV_FILE,
            mode="a",
            header=False,
            index=False
        )