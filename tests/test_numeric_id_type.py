from italian_csv_type_prediction.column_types.numeric_id_type import NumericIdType


def test_numeric_id_type():
    predictor = NumericIdType()
    assert all(predictor.validate([0, 1, 2, 4]))
    assert not any(predictor.validate([0, 1, 2, 40000]))
    assert not any(predictor.validate(
        ['16035', '1', '20100', '9', '11', '12', '13', '14']))
