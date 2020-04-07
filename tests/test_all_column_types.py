from italian_csv_type_prediction.column_types import AnyTypePredictor
from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from tqdm.auto import tqdm
import numpy as np

def test_all_column_types():
    """Test that predictors do not create false positives."""
    predictor = AnyTypePredictor()
    X = SimpleDatasetGenerator()
    for column_predictor in tqdm(predictor.predictors, desc="Testing predictors"):
        dataset = X.get_dataset(column_predictor)
        for candidate in tqdm([
            np.random.choice(dataset, size=np.random.randint(1, 100))
            for i in range(100)
        ], desc=f"Testing {column_predictor.name}"):
            assert column_predictor.validate(candidate)
