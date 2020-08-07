from italian_csv_type_prediction.simple_types import GenericItalianZIPCodeType


def test_generic_zip_code_type():
    predictor = GenericItalianZIPCodeType()
    assert predictor.validate("84100")
