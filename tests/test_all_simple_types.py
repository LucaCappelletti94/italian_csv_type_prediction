from italian_csv_type_prediction.column_types import AnyTypePredictor
from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from tqdm.auto import tqdm


def test_all_simple_types():
    """Test that predictors do not create false positives."""
    predictor = AnyTypePredictor()
    X = SimpleDatasetGenerator()
    for column_predictor in tqdm(predictor.predictors, desc="Testing predictors"):
        simple_predictor = column_predictor._main
        for candidate in tqdm(X.get_dataset(simple_predictor), desc=f"Testing {simple_predictor.name}"):
            if not simple_predictor.fuzzy:
                try:
                    assert simple_predictor.validate(candidate)
                except AssertionError as e:
                    print(f"Predictor {simple_predictor.name} was not able to correctly predict data from its dataset!")
                    print(f"A sample of the data is: {candidate}.")
                    raise e
                
