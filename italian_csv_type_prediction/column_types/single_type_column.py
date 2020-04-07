from .set_type_column import SetTypeColumnPredictor
from ..simple_types import (
    SimpleTypePredictor,
    CAPType as SimpleCAPType,
    AddressType as SimpleAddressType,
    BiologicalSexType as SimpleBiologicalSexType,
    BooleanType as SimpleBooleanType,
    CountryCodeType as SimpleCountryCodeType,
    CountryType as SimpleCountryType,
    DateType as SimpleDateType,
    EMailType as SimpleEMailType,
    FloatType as SimpleFloatType,
    IntegerType as SimpleIntegerType
)
from typing import List, Dict


class SingleTypeColumnPredictor(SetTypeColumnPredictor):
    def __init__(self, predictor: SimpleTypePredictor):
        """Create new Predictor based on a single type."""
        super().__init__([predictor])


class CAPType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleCAPType())


class AddressType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleAddressType())


class BiologicalSexType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleBiologicalSexType())


class BooleanType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleBooleanType())


class CountryCodeType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleCountryCodeType())


class CountryType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleCountryType())


class DateType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleDateType())


class EMailType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleEMailType())


class FloatType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleFloatType())


class IntegerType(SingleTypeColumnPredictor):
    def __init__(self):
        """Create new Predictor based on a single type."""
        super().__init__(SimpleIntegerType())
