from codicefiscale import codicefiscale
from italian_csv_type_prediction.simple_types import NameSurnameType, SurnameNameType


def test_namesurname():
    name_surname_predictor = NameSurnameType()
    surname_name_predictor = SurnameNameType()

    candidates = [
        ("Maria Teresa", "Lupi", None),
        ("NUNZIO", "SOFIA", "SFONNZ56T16A093W"),
        ("RINA", "BRUTTOMESSO", "BRTRNI67E57E349J"),
        ("LINO", "ANZOLIN", "NZLLNI74R09F964X"),
        ("MARIO", "CRISCUOLO", "CRSMRA70S13C129M"),
        ("GINO", "DONADELLO", "DNDGNI73E27E682L"),
        #("MARCO PIETRO", "BONATO", "BNTMRC34M28A093M"),
    ] 

    for name, surname, fiscal_code in candidates:
        if fiscal_code is None:
            fiscal_code = codicefiscale.encode(
                surname=surname, name=name, sex='M', birthdate='01/01/1990', birthplace='Roma')

        name_surname = f"{name} {surname}"
        surname_name = f"{surname} {name}"

        assert name_surname_predictor.validate(
            name_surname, fiscal_code=fiscal_code)
        assert surname_name_predictor.validate(
            surname_name, fiscal_code=fiscal_code)
        assert not name_surname_predictor.validate(
            surname_name, fiscal_code=fiscal_code)
        assert not surname_name_predictor.validate(
            name_surname, fiscal_code=fiscal_code)
