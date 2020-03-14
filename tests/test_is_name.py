from italian_csv_type_prediction.simple_types import is_name
from .utils import default_test


def test_is_name():
    default_test(is_name, ["names"], black_list=["regions", "provinces_codes", "countries", "country_codes", "surnames", "nans", "municipalities"])
