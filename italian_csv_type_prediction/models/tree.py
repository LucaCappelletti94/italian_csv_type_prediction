from ..datasets import load_nan, load_names, load_regions, load_countries, load_country_codes, load_municipalities, load_surnames, load_provinces_codes, load_caps, load_codice_fiscale, load_iva
from ..simple_types import is_any_type
import pandas as pd
import numpy as np
import os
import random
import pickle
from typing import List
from tqdm.auto import tqdm
from sklearn.preprocessing import LabelEncoder

tree = None
classes = [
    "NaN",
    "CAP",
    "ProvinceCode",
    "Region",
    "Municipality",
    "CodiceFiscale",
    "Year",
    "Country",
    "CountryCode",
    "Name",
    "Surname",
    "IVA"
]


def generate_training_set(subsets_number=1000, subsets_elements_number=40, error_probability=0.1):
    datasets = [
        tuple(load_nan()),
        tuple(load_caps()),
        tuple(load_provinces_codes()),
        tuple(load_regions()),
        tuple(load_municipalities()),
        tuple(load_codice_fiscale()),
        [
            random.randint(1950, 2050)
            for _ in range(1000)
        ],
        tuple(load_countries()),
        tuple(load_country_codes()),
        tuple(load_names()),
        tuple(load_surnames()),
        tuple(load_iva())
    ]
    datasets = list(zip(classes, datasets))
    X, Y = None, []
    for _ in tqdm(
        range(subsets_number),
        total=subsets_number,
        desc="Generating training dataset"
    ):
        main_dataset_name, dataset = random.choice(datasets)
        x = []
        for _ in range(subsets_elements_number):
            if random.uniform(0, 1) < 1-error_probability:
                x.append(random.choice(dataset))
                Y.append(main_dataset_name)
            else:
                tmp_dataset_name, tmp_dataset = random.choice(datasets)
                x.append(random.choice(tmp_dataset))
                Y.append(tmp_dataset_name)
        scores = compute_set_scores(x)
        if X is None:
            X = scores
        else:
            X = np.vstack([
                X,
                scores
            ])
    return X, [
        classes.index(y)
        for y in Y
    ]


def compute_set_scores(x: List[str]):
    df = pd.DataFrame([
        is_any_type(i)
        for i in x
    ])
    means = df.mean().values
    tiled = np.tile(means, (len(x), 1))
    return np.hstack([
        df.values,
        tiled
    ])


def load_tree():
    global tree
    if tree is None:
        with open("{}/tree.pkl".format(os.path.dirname(os.path.abspath(__file__))), "rb") as f:
            tree = pickle.load(f)
    return tree


def predict_types(x: List[str]) -> List[str]:
    """Return list of types of given list."""
    global classes
    return [
        classes[i]
        for i in load_tree().predict(compute_set_scores(x))
    ]
