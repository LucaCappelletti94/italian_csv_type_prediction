from typing import Dict, List

from .column_type_predictor import ColumnTypePredictor
from .single_type_column import (AddressType, BiologicalSexType, BooleanType,
                                 CAPType, CodiceFiscaleType, CountryCodeType,
                                 CountryType, CurrencyType, DateType,
                                 DocumentType, EMailType, FloatType,
                                 IntegerType, IVAType, MunicipalityType,
                                 NameType, NaNType, PhoneNumberType, PlateType,
                                 ProvinceCodeType, RegionType, StringType,
                                 SurnameType, YearType)


class AnyTypePredictor:
    def __init__(self):
        self._predictors = [
            predictor()
            for predictor in (
                AddressType, CAPType, CodiceFiscaleType, CountryCodeType,
                CountryType, CurrencyType, DateType, EMailType,
                FloatType, IntegerType, IVAType,
                MunicipalityType, NameType, NaNType, PhoneNumberType,
                ProvinceCodeType, RegionType, StringType, SurnameType,
                YearType, BiologicalSexType, BooleanType
            )
        ]

    @property
    def supported_types(self):
        """Return list of currently supported types."""
        return [
            predictor.name
            for predictor in self._predictors
        ]

    @property
    def predictors(self) -> List[ColumnTypePredictor]:
        return self._predictors

    def predict(self, values: List, **kwargs) -> Dict[str, List[bool]]:
        """Return prediction from all available type."""
        return {
            predictor.name: predictor.validate(values)
            for predictor in self._predictors
        }
