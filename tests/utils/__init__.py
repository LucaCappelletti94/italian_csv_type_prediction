import numpy as np
from italian_csv_type_prediction.datasets import load_provinces_codes, load_regions
from typing import List

cap = ["29121", "00121", 561, 29121]
dates = ["12/12/1994", "12 dicembre 1994", "12 dic 1994"]
nans = ["", 0, "Nan", ".", "-", np.nan]
regions = ["Emilia-romagna", "valle d'aosta"]
provinces_codes = ["pc"]

types = {
    "cap": cap,
    "dates": dates,
    "nans": nans,
    "regions": list(load_regions()) + regions,
    "provinces_codes": list(load_provinces_codes()) + provinces_codes
}


def get_type(t):
    return types[t]


def get_not_type(t):
    return [
        e
        for key, elements in types.items()
        if key != t
        for e in elements
    ]


def get_cases(t):
    return get_type(t), get_not_type(t)


def default_test(test, positives: List[str], negatives: List[str]=None):
    if negatives is None:
        negatives = list(set(types.keys()) - set(positives))

    for pos in positives:
        for t in types[pos]:
            if not test(t):
                raise AssertionError("Test {testname} on {positive} has failed.".format(
                    testname=test.__name__,
                    positive=t
                ))

    for neg in negatives:
        for t in types[neg]:
            if test(t):
                raise AssertionError("Test {testname} on {negative} has failed.".format(
                    testname=test.__name__,
                    negative=t
                ))
