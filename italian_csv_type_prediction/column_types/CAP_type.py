from .single_type_column import SingleTypeColumnPredictor
from ..simple_types import CAPType as SimpleCAPType
from typing import List, Dict


class CAPType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new CAP Predictor based on data within column."""
        super().__init__(SimpleCAPType())
