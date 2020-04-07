from .set_type_column import SetTypeColumnPredictor
from ..simple_types import IVAType as SimpleIVAType, CodiceFiscaleType as SimpleCodiceFiscaleType
from typing import List, Dict


class IVAType(SetTypeColumnPredictor):
    def __init__(self):
        """Create new IVA Predictor based on data within column."""
        self._iva = SimpleIVAType()
        super().__init__([
            self._iva,
            SimpleCodiceFiscaleType()
        ])

    def validate(self, values: List, **kwargs: Dict) -> List[bool]:
        if not super().validate(values, **kwargs):
            return [False]*len(values)
        return [
            self._iva.validate(value)
            for value in values
        ]
