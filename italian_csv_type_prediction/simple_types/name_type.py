from .string_type import StringType
from .partial_set_type_predictor import PartialSetTypePredictor
from ..datasets import load_names
from codicefiscale import codicefiscale


class NameType(StringType):

    def __init__(self, **kwargs):
        """Create new surname type predictor."""
        super().__init__()
        self._predictor = PartialSetTypePredictor(
            load_names(), normalize_values=True, **kwargs)

    @property
    def fuzzy(self):
        return True

    def validate(self, candidate, codice_fiscale: str = None, **kwargs) -> bool:
        """Return boolean representing if given candidate is a valid italian name."""
        if not super().validate(candidate, **kwargs):
            return False
        if codice_fiscale is None:
            return self._predictor.validate(candidate)

        characters = codicefiscale.decode(
            codice_fiscale
        )["raw"]["name"]
        
        return all(
            character in candidate.lower()
            for character in characters.rstrip("X").lower()
        )
