from italian_csv_type_prediction.simple_types import is_region
from .utils import default_test


def test_is_region():
    default_test(is_region, ["regions"], black_list=["municipalities"])
