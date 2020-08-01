from italian_csv_type_prediction.column_types import AnyTypePredictor
from italian_csv_type_prediction.dataframe_generators import SimpleDatasetGenerator
from tqdm.auto import tqdm
import numpy as np


def test_all_column_types():
    """Test that predictors do not create false positives."""
    predictor = AnyTypePredictor()
    X = SimpleDatasetGenerator(verbose=True)
    success = True

    known_collisions = {
        "ItalianZIPCode": [
            "Integer",
            "Year",
        ],
        "Name": [
            "Country",
            "BiologicalSex"
        ],
        "Surname": [
            "BiologicalSex",
            "Document"
        ],
        "Integer": [
            "ItalianZIPCode",
            "Boolean",
            "ItalianVAT"
        ],
        "Float": [
            "ItalianZIPCode",
            "Boolean",
            "ItalianVAT"
        ],
        "PhoneNumber": [
            "ItalianVAT"
        ],
        "CountryCode": [
            "Boolean",
            "ProvinceCode"
        ],
        "ProvinceCode": [
            "Boolean",
            "CountryCode"
        ]
    }
    
    without_dataset = set([
        "SurnameName",
        "NameSurname",
        "Name",
        "Surname",
        "Company",
        "String",
        "NaN"
    ])

    for column_predictor in tqdm(predictor.predictors, desc="Testing predictors"):
        if column_predictor.name in without_dataset:
            continue
        for sub_predictor in tqdm(predictor.predictors, desc=f"Datasets", leave=False):
            if sub_predictor.name in without_dataset:
                continue
            if isinstance(column_predictor._main, sub_predictor._main.__class__):
                continue
            if isinstance(sub_predictor._main, column_predictor._main.__class__):
                continue
            if sub_predictor.name in known_collisions.get(column_predictor.name, []):
                continue
            dataset = X.get_dataset(sub_predictor)
            candidates = [np.random.choice(
                dataset, size=np.random.randint(5, 30)) for i in range(500)]
            for candidate in tqdm(candidates, leave=False, desc=f"Test {column_predictor.name} on {sub_predictor.name} dataset"):
                try:
                    prediction = np.array(column_predictor.validate(candidate))
                    if column_predictor == sub_predictor:
                        assert np.all(prediction)
                    else:
                        assert not np.any(prediction)
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
