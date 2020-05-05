from .string_type import SimpleTypePredictor
from ..datasets import load_address_starters


class AddressType(SimpleTypePredictor):

    def __init__(self):
        self._words = load_address_starters()

    @property
    def fuzzy(self) -> bool:
        return True

    def validate(self, candidate, **kwargs) -> bool:
        candidate = str(candidate)
        return any(candidate.startswith(e) for e in self._words)