import pandas as pd
from typing import Dict
from ..utils import TranslateType


class PlaceholderExtractor:

    def __init__(self, transate_types: bool = True):
        self._translator = TranslateType()
        self._transate_types = transate_types

    def _to_placeholder(self, value, value_type) -> Dict:
        if self._transate_types:
            value_type = self._translator.transate(value_type)
        return {
            "placeholder": "{{{value_type}}}".format(value_type=value_type),
            "values": {
                value_type: value
            }
        }

    def extract(self, df: pd.DataFrame, types: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame({
            column: [
                self._to_placeholder(value, value_type)
                for value, value_type in zip(df[column], types[column])
            ]
            for column in df.columns
        })
