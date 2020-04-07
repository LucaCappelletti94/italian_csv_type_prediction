from money_parser import price_str
from .string_type import StringType
from .plate_type import PlateType
from .IVA_type import IVAType


class CurrencyType(StringType):
    def __init__(self):
        super().__init__()
        self._plate = PlateType()

    def validate(self, candidate, **kwargs) -> bool:
        if str(candidate).startswith("0"):
            return False
        if not super().validate(candidate, **kwargs) or self._plate.validate(candidate):
            return False
        try:
            candidate = price_str(str(candidate))
            return len(str(float(candidate)).split(".")[-1]) <= 2
        except (ValueError, TypeError):
            return False
