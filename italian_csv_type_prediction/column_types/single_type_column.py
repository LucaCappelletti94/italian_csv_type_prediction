from .column_type_predictor import ColumnTypePredictor
from ..simple_types.simple_type import SimpleTypePredictor
from typing import List, Dict


class SingleTypeColumnPredictor(ColumnTypePredictor):
    def __init__(self, predictor: SimpleTypePredictor):
        super().__init__([predictor])
