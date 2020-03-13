from italian_csv_type_prediction.simple_types import is_municipality
from .utils import default_test


def test_is_municipality():
    default_test(is_municipality, ["municipalities"], black_list=["regions", "provinces_codes", "countries", "country_codes"])
