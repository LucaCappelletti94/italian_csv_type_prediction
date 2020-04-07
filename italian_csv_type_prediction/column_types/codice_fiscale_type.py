from .set_type_column import SetTypeColumnPredictor
from ..simple_types import IVAType as SimpleIVAType, CodiceFiscaleType as SimpleCodiceFiscaleType
from typing import List, Dict


class CodiceFiscaleType(SetTypeColumnPredictor):
    def __init__(self):
        """Create new CodiceFiscale Predictor based on data within column."""
        self._codife_fiscale = SimpleCodiceFiscaleType()
        super().__init__([
            self._codife_fiscale,
            SimpleIVAType()
        ])

    def validate(self, values: List, **kwargs: Dict) -> List[bool]:
        if not super().validate(values, **kwargs):
            return False
        return [
            self._codife_fiscale.validate(value)
            for value in values
        ]
