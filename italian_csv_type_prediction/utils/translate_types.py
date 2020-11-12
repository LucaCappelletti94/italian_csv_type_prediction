import compress_json
import pandas as pd
from typing import Tuple, List, Union


class TranslateType:

    SUPPORTED_LANGUAGES = ("it", )
    ERROR_HANDLING = ("raise", "pass")

    def __init__(self, language: str = "it", error_handling: str = "raise"):
        """Create new object to translate types to given language.

        Parameters
        ----------------------
        language: str = "it",
            The language to translate the strings to.
            Currently supporting only italian language.
        error_handling: str = "raise",
            Behaviour of the translator when a given string is not available.
            The possible behaviours are 'raise' or 'pass'.
            The default behaviour is 'raise'.

        Raises
        ----------------------
        ValueError,
            When the given language is not supported.
        ValueError,
            When the given error handling is not supported.
        """
        if language not in TranslateType.SUPPORTED_LANGUAGES:
            raise ValueError(
                (
                    "Given language '{language}' is not supported. "
                    "The supported languages are {supported_languages}."
                ).format(
                    language=language,
                    supported_languages=", ".join(
                        TranslateType.SUPPORTED_LANGUAGES
                    )
                )
            )
        if error_handling not in TranslateType.ERROR_HANDLING:
            raise ValueError(
                (
                    "Given error handling '{error_handling}' is not supported. "
                    "The supported error handling are {supported_error_handlings}."
                ).format(
                    error_handling=error_handling,
                    supported_error_handlings=", ".join(
                        TranslateType.ERROR_HANDLING
                    )
                )
            )
        self._translations = compress_json.local_load(
            "{}.json".format(language)
        )
        self._error_handling = error_handling
        self._reverse_translations = {
            v: k
            for k, v in self._translations.items()
        }

    def translate(self, value_type: Union[List, Tuple]) -> str:
        """Return value type translated to given language.

        Parameters
        ----------------------
        value_type: Union[str, List, Tuple],
            Either the value to be translated or a list of values.

        Raises
        ----------------------
        ValueError,
            If the value is not available in the dictionary.

        Returns
        ----------------------
        The translated value.
        """
        if isinstance(value_type, (list, tuple)):
            return tuple([
                self.translate(v)
                for v in value_type
            ])
        if value_type not in self._translations:
            if self._error_handling == "raise":
                raise ValueError(
                    "The given value {} is not available in the dictionary.".format(
                        value_type
                    )
                )
            if self._error_handling == "pass":
                return value_type
        return self._translations[value_type]

    def reverse_translate(self, value_type: Union[str, List, Tuple]) -> str:
        """Return value type translated back to english from given language.

        Parameters
        ----------------------
        value_type: Union[str, List, Tuple],
            Either the value to be back translated or a list of values.

        Raises
        ----------------------
        ValueError,
            If the value is not available in the dictionary.

        Returns
        ----------------------
        The back translated value.
        """
        if isinstance(value_type, (list, tuple)):
            return tuple([
                self._reverse_translations(v)
                for v in value_type
            ])
        if value_type not in self._reverse_translations:
            if self._error_handling == "raise":
                raise ValueError(
                    "The given value {} is not available in the dictionary.".format(
                        value_type
                    )
                )
            if self._error_handling == "pass":
                return value_type
        return self._reverse_translations[value_type]

    def translate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Translate all dataframe."""
        return df.applymap(self.translate)
