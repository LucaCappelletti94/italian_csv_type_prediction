from .extractor import Extractor
from ..simple_types import (FuzzyItalianZIPCodeType,
                            MunicipalityType, CountryType, RegionType)
from .default_extractor import DefaultExtractor
from typing import Dict
import compress_json
import re


class AddressExtractor(Extractor):

    def __init__(self, symbols_to_strip_on_collision=":@-,.", **kwargs):
        """Create new AddressExtractor object.

        Parameters
        ----------------------------
        symbols_to_strip_on_collision: str = ":@-,.",
            List of the symbols to remove out of the address in situation of
            collisions caused by misplaced symbols that are removed within
            the postal library.
        """
        super().__init__(**kwargs)
        self._default_extractor = DefaultExtractor(**kwargs)
        self._mapping = compress_json.local_load("libpostal_mapping.json")
        self._symbols_to_strip_on_collision = symbols_to_strip_on_collision
        self._validators = {
            "ItalianZIPCode": FuzzyItalianZIPCodeType(),
            "Municipality": MunicipalityType(),
            "Country": CountryType(),
            "Region": RegionType()
        }

        self._unsupported = [
            "city_district", "unit", "state_district"
        ]

    def extract(self, candidate: str, candidate_type: str, **kwargs) -> Dict:
        from postal.parser import parse_address

        lower = candidate.lower()
        parsed = parse_address(
            candidate, language="IT", country="IT")

        has_errored = False

        for _, key in parsed:
            if key in self._unsupported:
                has_errored = True
                break

        if has_errored:
            return self._default_extractor.extract(
                candidate, candidate_type, **kwargs
            )

        updated_parsed = {}
        for value, prediction in parsed:
            # If the given candidate in lowercase contains the value
            # we can simply identify it and replace it.
            if value in lower:
                updated_parsed[self._mapping[prediction]] = [
                    candidate[
                        lower.find(value):lower.find(value)+len(value)
                    ]
                ]

        for key, (value,) in updated_parsed.items():
            if key in self._validators:
                if not self._validators[key].validate(value):
                    has_errored = True
                    break

        if has_errored:
            return self._default_extractor.extract(
                candidate, candidate_type, **kwargs
            )

        return self.build_dictionary(
            candidate=candidate,
            values=updated_parsed
        )
