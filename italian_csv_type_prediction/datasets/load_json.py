import compress_json
import os

datasets = {}


def load_local_json_sets(path: str):
    if path not in datasets:
        datasets[path] = set(compress_json.load("{pwd}/{path}.json.gz".format(
            pwd=os.path.dirname(os.path.abspath(__file__)),
            path=path
        )))
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


def load_caps():
    return load_local_json_sets("caps")


def load_codice_fiscale():
    return load_local_json_sets("codice_fiscale")


def load_iva():
    return load_local_json_sets("iva")


def load_strings():
    return load_local_json_sets("strings")


def load_email():
    return load_local_json_sets("email")


def load_phone():
    return load_local_json_sets("phone")
