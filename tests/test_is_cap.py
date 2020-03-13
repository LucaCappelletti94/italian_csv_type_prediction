from italian_csv_type_prediction.simple_types import is_cap
import numpy as np

def test_is_cap():
    caps = [
        "29121", "00121", 561, 29121
    ]
    non_caps = [
        "ciao", "Luca", "", 0, "Nan", ".", "-", np.nan, 4545451
    ]

    assert all([
        is_cap(value)
        for value in caps
    ])
    assert all([
        not is_cap(value)
        for value in non_caps
    ])
