from .integer_type import IntegerType
from .italian_zip_code_type import ItalianZIPCodeType
from ..datasets import load_caps


class FuzzyItalianZIPCodeType(ItalianZIPCodeType):

    def convert(self, candidate) -> str:
        """Convert given candidate to CAP."""
        return super().convert(candidate).zfill(5)

    def validate(self, candidate, **kwargs) -> bool:
        """Return boolean representing if given candidate matches regex for CAP values."""
        return super().validate(self.convert(candidate))
