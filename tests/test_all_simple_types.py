from italian_csv_type_prediction.column_types import AnyTypePredictor
from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from italian_csv_type_prediction.simple_types import FuzzyItalianZIPCodeType, FuzzyGenericItalianZIPCodeType, GenericItalianZIPCodeType
from italian_csv_type_prediction.utils import normalize
from tqdm.auto import tqdm


def test_all_simple_types():
    """Test that predictors do not create false positives."""
    predictor = AnyTypePredictor()
    X = SimpleDatasetGenerator()

    aliases = {
        "ItalianZIPCode": [
            FuzzyItalianZIPCodeType(),
            FuzzyGenericItalianZIPCodeType(),
            GenericItalianZIPCodeType()
        ]
    }

    errors = 0

    without_dataset = [
        "SurnameName",
        "NameSurname",
        "Name",
        "Surname",
        "Company"
    ]

    for column_predictor in tqdm(predictor.predictors, desc="Testing predictors"):
        simple_predictor = column_predictor._main
        if simple_predictor.name in without_dataset:
            continue
        for candidate in X.get_dataset(simple_predictor):
            try:
                assert simple_predictor.validate(candidate) or any(
                    pred.validate(candidate)
                    for pred in aliases.get(simple_predictor.name, [])
                )
            except AssertionError:
                errors += 1
                print(
                    f"Predictor {simple_predictor.name} was not able to correctly predict data from its dataset!")
                print(f"The data were the failure happened was: {candidate}, {normalize(candidate)}.")
    if errors:
        print(f"There were {errors} errors!")
    assert not errors
