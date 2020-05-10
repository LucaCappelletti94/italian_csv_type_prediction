import pandas as pd
from typing import Dict
from .name_surname_extractor import NameSurnameExtractor
from .surname_name_extractor import SurnameNameExtractor
from .default_extractor import DefaultExtractor
from ..embedding import DataframeEmbedding

class PlaceholderExtractor:

    def __init__(self):
        extractors = [
            extractor()
            for extractor in (NameSurnameExtractor, SurnameNameExtractor)
        ]
        self._default = DefaultExtractor()
        self._embedding = DataframeEmbedding()
        self._extractors = {
            extractor.name:extractor
            for extractor in extractors
        }

    def _handle_value_extraction(self, candidate:str, candidate_type:str, **kwargs)->Dict:
        try:
            return self._extractors.get(candidate_type, self._default).extract(
                candidate=candidate,
                candidate_type=candidate_type,
                **kwargs
            )
        except ValueError:
            return self._default.extract(candidate, "Error")


    def extract(self, df: pd.DataFrame, types: pd.DataFrame) -> pd.DataFrame:
        fiscal_codes = self._embedding.get_fiscal_codes(df)
        italian_vat_codes = self._embedding.get_italian_vat_codes(df)
        return pd.DataFrame({
            column: [
                self._handle_value_extraction(
                    candidate=candidate,
                    candidate_type=candidate_type,
                    fiscal_codes=fiscal_codes,
                    italian_vat_codes=italian_vat_codes
                )
                for candidate, candidate_type in zip(df[column], types[column])
            ]
            for column in df.columns
        })
