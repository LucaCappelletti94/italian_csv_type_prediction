import pandas as pd
from typing import Dict


def to_placeholder(value, value_type) -> Dict:
    return {
        "placeholder": "{{{value_type}}}".format(value_type=value_type),
        "values": {
            value_type: value
        }
    }


def extract_placeholders(df: pd.DataFrame, types: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        column: [
            to_placeholder(value, value_type)
            for value, value_type in zip(df[column], types[column])
        ]
        for column in df.columns
    })
