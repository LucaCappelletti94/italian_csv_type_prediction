import json
import os

datasets = {}


def load_local_json(path: str):
    if path not in datasets:
        json_path = "{pwd}/{path}.json".format(
            pwd=os.path.dirname(os.path.abspath(__file__)),
            path=path
        )
        with open(json_path, "r") as f:
            datasets[path] = json.load(f)
    return datasets[path]


def load_nan():
    return load_local_json("nan")
