from italian_csv_type_prediction.simple_types import is_date
import numpy as np

def test_is_date():
    date = [
        "12/12/1994", "12 dicembre 1994", "12 dic 1994"
    ]
    non_date = [
        67, "ciao", "Luca", "", 0, "date", ".", "-", np.nan
    ]

    assert all([
        is_date(value)
        for value in date
    ])
    assert all([
        not is_date(value)
        for value in non_date
    ])
