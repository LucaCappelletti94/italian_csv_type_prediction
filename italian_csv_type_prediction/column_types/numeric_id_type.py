from .single_type_column import SingleTypeColumnPredictor
from ..simple_types import IntegerType
from typing import List, Dict


class NumericIdType(SingleTypeColumnPredictor):

    def __init__(self, density: float = 0.9):
        """Create new NumericId Predictor based on data within column.

        Parameters
        --------------------------
        density: float = 0.9,
            Minimal density from minimum integer to maximum integer.
        """
        super().__init__(IntegerType())
        self._density = density

    def validate(self, values: List, **kwargs: Dict) -> List[bool]:
        """Return list of booleans representing, for each value, if are indices."""
        if super().validate(values, **kwargs):
            return False

        are_integers = [
            self._predictor.validate(value)
            for value in values
        ]
            
        integer_values = [
            self._predictor.convert(value)
            for value, is_integer in zip(values, are_integers)
            if is_integer
        ]

        _min, _max = min(integer_values), max(integer_values)

        unique_values = len(set(integer_values))

        are_indices = unique_values / (_max - _min) >= self._density

        return [
            are_indices and is_integer
            for is_integer in are_integers
        ]
