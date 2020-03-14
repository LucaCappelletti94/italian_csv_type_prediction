import json
import os

datasets = {}


def load_local_json_sets(path: str):
    if path not in datasets:
        json_path = "{pwd}/{path}.json".format(
            pwd=os.path.dirname(os.path.abspath(__file__)),
            path=path
        )
        with open(json_path, "r", encoding="utf8") as f:
            datasets[path] = set(json.load(f))
    return datasets[path]


def load_nan():
    return load_local_json_sets("nan")


def load_provinces_codes():
    return load_local_json_sets("provinces_codes")


def load_regions():
    return load_local_json_sets("regions")


def load_municipalities():
    return load_local_json_sets("municipalities")


def load_countries():
    return load_local_json_sets("countries")


def load_country_codes():
    return load_local_json_sets("country_codes")

def load_surnames():
    return load_local_json_sets("surnames")

def load_names():
    return load_local_json_sets("names")