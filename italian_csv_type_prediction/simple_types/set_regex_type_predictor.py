from .regex_type_predictor import RegexTypePredictor
import re
from ..utils import normalize
from typing import List


class SetRegexTypePredictor(RegexTypePredictor):

    def __init__(self, words: List[str]):
        """Create new set regex based predictor.

        Parameters
        --------------------------------
        pattern: str,
            The pattern against which to test.
        """
        super().__init__(r"(?:\W|\b)(?:{})(?:\W|\b)".format("|".join([
            re.escape(normalize(word))
            for word in words
        ])))
