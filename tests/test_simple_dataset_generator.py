from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from italian_csv_type_prediction.column_types import AnyTypePredictor
from italian_csv_type_prediction.features import AnyFeature
import pandas as pd

pd.options.mode.chained_assignment = "raise"


def test_simple_dataset_builder():
    dataset = SimpleDatasetGenerator()
    features = AnyFeature()
    simple_predictor = AnyTypePredictor()
    assert set(list(dataset._datasets.keys()) + ["NaN"]) == set(
        simple_predictor.supported_types)

    available_types_number = len(simple_predictor.supported_types)
    available_features_number = len(features.supported_features)

    X, y = dataset.build(10)

    assert X.shape[0] == y.size
    assert X.shape[1] == (available_types_number+available_features_number)*2
