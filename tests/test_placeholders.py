from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from italian_csv_type_prediction import TypePredictor, PlaceholderExtractor


def test_type_predictor():
    dataset = SimpleDatasetGenerator()
    model = TypePredictor()
    df, _ = dataset.generate_simple_dataframe()
    predictions = model.predict_dataframe(df)

    extractor = PlaceholderExtractor()

    extractor.extract(df, predictions)