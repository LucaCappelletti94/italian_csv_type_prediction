from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from italian_csv_type_prediction.simple_types import AnySimpleTypePredictor
import pandas as pd

pd.options.mode.chained_assignment = "raise"


def test_simple_dataset_builder():
    dataset = SimpleDatasetGenerator()
    simple_predictor = AnySimpleTypePredictor()
    assert set(list(dataset._datasets.keys())) == set(
        simple_predictor.supported_types)

    available_types_number = len(simple_predictor.supported_types)

    X, y = dataset.build(10)

    assert X.shape[0] == y.size
    assert X.shape[1] == available_types_number*2
