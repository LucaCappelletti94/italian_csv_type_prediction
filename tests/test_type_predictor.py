from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from italian_csv_type_prediction.models import TypePredictor
import pandas as pd

pd.options.mode.chained_assignment = "raise"


def test_type_predictor():
    dataset = SimpleDatasetGenerator()
    model = TypePredictor(local_path="test.pkl.gz")
    model.fit(number=10)

    df, _ = dataset.generate_simple_dataframe()

    model.predict_dataframe(df)

    model = TypePredictor(local_path="test.pkl.gz")
