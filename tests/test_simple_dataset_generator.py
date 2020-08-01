from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from italian_csv_type_prediction.column_types import AnyTypePredictor
import pandas as pd

pd.options.mode.chained_assignment = "raise"


def test_simple_dataset_builder():
    dataset = SimpleDatasetGenerator()
    simple_predictor = AnyTypePredictor()
    assert set(list(dataset._datasets.keys()) + ["NaN", "NameSurname", "SurnameName", "Name", "Surname", "Company"]) == set(
        simple_predictor.supported_types)

    available_types_number = len(simple_predictor.supported_types)

    X, y = dataset.build(10)

    assert X.shape[0] == y.size
    assert X.shape[1] == (available_types_number)*2
