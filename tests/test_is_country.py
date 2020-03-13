from italian_csv_type_prediction.simple_types import is_country
from .utils import default_test


def test_is_country():
    default_test(is_country, ["countries"], black_list=["municipalities"])
