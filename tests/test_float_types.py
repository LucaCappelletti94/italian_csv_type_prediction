from italian_csv_type_prediction.simple_types import FloatType
import numpy as np


def test_float_type():
    predictor = FloatType()

    valids = [
        0,
        1.0,
        3.14,
        0.125,
        "1.000.000.00"
    ]
    invalids = [
        "ciao",
        "12.12.94",
        "12.12.1994",
        "2017, 2016",
        "2017, 2016, 2019",
        False,
        True,
        None,
        np.nan
    ]

    for valid in valids:
        assert predictor.validate(valid)
        assert predictor.validate(str(valid))

    for invalid in invalids:
        try:
            assert not predictor.validate(invalid)
            assert not predictor.validate(str(invalid))
        except AssertionError as e:
            print("Invalid value {} predicted as valid.".format(invalid))
            raise e