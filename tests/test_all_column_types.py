from italian_csv_type_prediction.column_types import AnyTypePredictor
from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from tqdm.auto import tqdm
import numpy as np


def test_all_column_types():
    """Test that predictors do not create false positives."""
    predictor = AnyTypePredictor()
    X = SimpleDatasetGenerator()
    success = True

    known_collisions = {
        "CAP": [
            "Integer",
            "Year",
            "NumericId"
        ],
        "Name":[
            "Country",
            "BiologicalSex"
        ],
        "Surname":[
            "BiologicalSex",
            "Document"
        ],
        "Integer":[
            "CAP",
            "Boolean",
            "IVA"
        ],
        "Float":[
            "CAP",
            "Boolean",
            "IVA"
        ],
        "PhoneNumber":[
            "IVA"
        ],
        "CountryCode":[
            "Boolean",
            "ProvinceCode"
        ],
        "ProvinceCode":[
            "Boolean",
            "CountryCode"
        ],
        "Currency":[
            "Year",
            "Float",
            "Integer",
            "CAP",
            "NumericId",
            "Boolean"
        ]
    }

    for column_predictor in tqdm(predictor.predictors, desc="Testing predictors"):
        if column_predictor.name in ("String", "NaN"):
            continue
        for sub_predictor in predictor.predictors:
            if sub_predictor.name in ("NaN"):
                continue
            if isinstance(column_predictor._main, sub_predictor._main.__class__):
                continue
            if isinstance(sub_predictor._main, column_predictor._main.__class__):
                continue
            if sub_predictor.name in known_collisions.get(column_predictor.name, []):
                continue
            dataset = X.get_dataset(sub_predictor)
            for candidate in [np.random.choice(dataset, size=np.random.randint(5, 30)) for i in range(500)]:
                try:
                    prediction = np.array(column_predictor.validate(candidate))
                    if column_predictor == sub_predictor:
                        assert all(prediction)
                    else:
                        assert not any(prediction)
                except AssertionError:
                    success = False
                    error_type = "False negative" if column_predictor == sub_predictor else "False positive"
                    print(
                        f"Predictor {column_predictor.name} was not able to correctly predict data from {sub_predictor.name}.")
                    print(f"The error is a {error_type}")
                    if column_predictor == sub_predictor:
                        print(
                            f"A sample of the data is: {candidate[~prediction]}.")
                    else:
                        print(
                            f"A sample of the data is: {candidate[prediction]}.")
                    print("="*50)
    assert success
