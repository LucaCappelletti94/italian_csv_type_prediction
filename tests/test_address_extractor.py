from italian_csv_type_prediction.mixed_types.address_extractor import AddressExtractor
from italian_csv_type_prediction.datasets import load_address

def test_address_extractor():
    extractor = AddressExtractor()

    strange_addresses = [
        "VIA COLLE DELL'ASSIETTA 23",
        "Piazza S. Marco, 17 25088 TOSCOLANO MADERNO",
        "Via 25 aprile 1945 n. 39/A",
        "Via 25 aprile 1945 n. 15",
        "Via Pralongo, 64/C-10 31050 Monastier di treviso",
        "Viale Nino Bixio, 31 - 31100 Treviso",
        "Via San Pio X, 25 - 31056 Roncade"
    ]

    adresses = load_address()

    for candidate in strange_addresses + adresses:
        extractor.extract(candidate, None)
