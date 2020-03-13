from italian_csv_type_prediction.simple_types import is_province_code
from .utils import default_test


def test_is_province_code():
    default_test(is_province_code, ["provinces_codes"], black_list=["municipalities", "country_codes"])
