from .column_type_predictor import ColumnTypePredictor
from ..simple_types.simple_type import SimpleTypePredictor
from ..simple_types.nan_type import NaNType
from typing import List, Dict


class SetTypeColumnPredictor(ColumnTypePredictor):
    def __init__(self, predictors: List[SimpleTypePredictor]):
        self._predictors = predictors + NaNType()

    def validate(self, values: List, **kwargs: Dict) -> List[bool]:
        """Return list of booleans representing if each value has been identified.

        Parameters
        -----------------------------------
        values:List,
            List of other values in the column.
        kwargs:Dict,
            Additional features to be considered.
        """
        return all([
            any(predictor.validate(value) for predictor in self._predictors)
            for value in values
        ])
