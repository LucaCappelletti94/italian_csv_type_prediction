from .full_name_type import FullNameType
from typing import Tuple


class NameSurnameType(FullNameType):

    def _convert(self, name: str, surname: str) -> Tuple[str, str]:
        return name, surname

    def _validate(self, name: str, surname: str, fiscal_code: str = None, **kwargs) -> bool:
        return self._name.validate(name) and self._surname.validate(surname)
