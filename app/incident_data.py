import pandas as pd
from typing import List

def load_incidents_from_csv(path: str) -> List[str]:
    df = pd.read_csv(path)
    return df["log_text"].dropna().tolist()