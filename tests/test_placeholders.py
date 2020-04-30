from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from italian_csv_type_prediction import TypePredictor, extract_placeholders


def test_type_predictor():
    dataset = SimpleDatasetGenerator()
    model = TypePredictor()
    df, _ = dataset.generate_simple_dataframe()
    predictions = model.predict_dataframe(df)

    extract_placeholders(df, predictions)