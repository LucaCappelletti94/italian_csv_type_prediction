from money_parser import price_str
from .is_float import is_float

def is_euro(candidate) -> bool:
    if isinstance(candidate, str) and candidate.startswith("0"):
        return False
    if is_float(candidate):
        return len(str(candidate).split(".")[-1]) <= 2
    try:
        candidate = price_str(str(candidate))
        return len(str(float(candidate)).split(".")[-1]) <= 2
    except (ValueError, TypeError):
        return False
