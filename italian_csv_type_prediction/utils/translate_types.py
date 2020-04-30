import compress_json
import pandas as pd


class TranslateType:

    def __init__(self):
        """Create new object to translate types to Italian."""
        self._translations = compress_json.local_load("translations.json")

    def transate(self, value_type: str) -> str:
        """Return value type translated to Italian."""
        return self._translations[value_type]

    def transate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Translate all dataframe."""
        return df.applymap(self.transate)
