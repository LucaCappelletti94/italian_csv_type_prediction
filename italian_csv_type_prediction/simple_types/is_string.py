from .is_nan import is_nan
from .is_integer import is_integer
from .is_float import is_float
from .is_euro import is_euro

def is_string(candidate):
    if not isinstance(candidate, str):
        return False
    if any(test(candidate) for test in (is_nan, is_integer, is_float, is_euro)):
        return False
    return True