from ..datasets import load_surnames
from ..utils import normalize_string


def is_surname(candidate) -> bool:
    """Return boolean representing if given candidate is a valid italian surname."""
    return isinstance(candidate, str) and load_surnames() > set((normalize_string(candidate).lower(),))
