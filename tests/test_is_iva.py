from italian_csv_type_prediction.simple_types import is_iva
from .utils import default_test


def test_is_iva():
    default_test(is_iva, ["iva"])