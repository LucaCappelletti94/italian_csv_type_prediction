from ..datasets import load_names
from ..utils import normalize_string


def is_name(candidate) -> bool:
    """Return boolean representing if given candidate is a valid italian name."""
    return isinstance(candidate, str) and load_names() > set((normalize_string(candidate).lower(),))
