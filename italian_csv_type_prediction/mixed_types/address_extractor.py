from .extractor import Extractor
from postal.parser import parse_address
from ..simple_types import FuzzyItalianZIPCodeType, MunicipalityType
from typing import Dict
import compress_json


class AddressExtractor(Extractor):

    def __init__(self):
        super().__init__()
        self._mapping = compress_json.local_load("libpostal_mapping.json")
        self._validators = {
            "ItalianZIPCodeType": FuzzyItalianZIPCodeType(),
            "Municipality": MunicipalityType()
        }

    def extract(self, candidate: str, candidate_type: str, **kwargs) -> Dict:
        lower = candidate.lower()
        parsed = {
            self._mapping[prediction]: [
                candidate[
                    lower.find(value):lower.find(value)+len(value)
                ]
            ]
            for value, prediction in parse_address(candidate)
        }

        errors = []

        for key, (value,) in parsed.items():
            if key in self._validators:
                if not self._validators[key].validate(value):
                    errors.append(value)
                    del parsed[key]

        return self.build_dictionary(
            candidate=candidate,
            values={
                **parsed,
                **({"Error": errors} if errors else {})
            }
        )
