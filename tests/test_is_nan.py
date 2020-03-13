from italian_csv_type_prediction.simple_types import is_nan
import numpy as np

def test_is_nan():
    nans = [
        "", 0, "Nan", ".", "-", np.nan
    ]
    non_nans = [
        67, "ciao", "Luca"
    ]

    assert all([
        is_nan(value)
        for value in nans
    ])
    assert all([
        not is_nan(value)
        for value in non_nans
    ])
