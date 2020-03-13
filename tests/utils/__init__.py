import numpy as np
from italian_csv_type_prediction.datasets import load_provinces_codes, load_regions, load_municipalities
from typing import List

cap = ["29121", "00121", 561, 29121]
dates = ["12/12/1994", "12 dicembre 1994", "12 dic 1994"]
nans = ["", 0, "Nan", ".", "-", np.nan, None]
regions = ["Emilia-romagna", "valle d'aosta"]
municipalities = ["Piacenza", "Ferriere"]
provinces_codes = ["pc"]
iva = ["00380210302", "02005780131", "02437800135", "IT02437800135", 2437800135]

types = {
    "cap": cap,
    "dates": dates,
    "nans": nans,
    "iva": iva,
    "regions": list(load_regions()) + regions,
    "municipalities":list(load_municipalities()) + municipalities,
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


def default_test(test, positives: List[str], negatives: List[str]=None, black_list: List[str]=()):
    if negatives is None:
        negatives = list(set(types.keys()) - set(positives) - set(black_list))

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
