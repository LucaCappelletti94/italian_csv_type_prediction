import re
from .is_nan import is_nan

cap_regex = re.compile(r"^\d{5}$")

def is_cap(candidate)->bool:
    """Return a boolean representing if given candidate is a valid italian CAP."""
    if isinstance(candidate, (str, int, float)):
        return bool(cap_regex.match(str(candidate).zfill(5))) and not is_nan(candidate)
    return False