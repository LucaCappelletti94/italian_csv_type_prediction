import compress_json

def test_translations_pypostal():
    postal_mapping = compress_json.load(
        "italian_csv_type_prediction/mixed_types/libpostal_mapping.json"
    )
    translations = compress_json.load(
        "italian_csv_type_prediction/utils/it.json"
    )
    assert set(postal_mapping.values()) < set(translations.keys())