from italian_csv_type_prediction.simple_types import IntegerType
import numpy as np


def test_integer_type():
    predictor = IntegerType()

    valids = [
        3,
        6,
        0,
        "1.000.000.00"
    ]
    invalids = [
        "ciao",
        "12.12.94",
        "12.12.1994",
        False,
        True,
        None,
        np.nan
    ]

    for valid in valids:
        assert predictor.validate(valid)
        assert predictor.validate(str(valid))

    for invalid in invalids:
        assert not predictor.validate(invalid)
        assert not predictor.validate(str(invalid))
