from italian_csv_type_prediction.simple_types import is_country_code
from .utils import default_test


def test_is_country_code():
    default_test(is_country_code, ["country_codes"], black_list=["provinces_codes", "municipalities"])
