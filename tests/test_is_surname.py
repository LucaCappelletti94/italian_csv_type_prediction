from italian_csv_type_prediction.simple_types import is_surname
from .utils import default_test


def test_is_surname():
    default_test(is_surname, ["surnames"], black_list=["regions", "provinces_codes", "countries", "country_codes", "names", "nans", "municipalities"])