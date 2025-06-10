from dataclasses import dataclass
from typing import List

from cipher.base import CipherBit
from cipher.interfaces import CipherTable
from utils.tools import remove_duplicates, filter_allowed_chars
from utils.validators import ensure_not_empty

@dataclass(kw_only=True)
class Vigenere(CipherBit):
    """
    Vigenère cipher using a composable CipherTable for substitution logic.

    This class does not construct its own tabula recta; instead, it delegates
    all key-based mapping logic to the provided CipherTable object.
    """
    keyword: List[str]
    table: CipherTable

    def __post_init__(self):
        super().__post_init__()
        self.keyword = remove_duplicates(
            filter_allowed_chars(self.keyword, set(self.table.base_alphabet))
        )
        ensure_not_empty(self.keyword, "Keyword must not be empty")

    def _transform(self, decrypt: bool) -> List[str]:
        result = []
        key = self.keyword
        klen = len(key)

        for i, char in enumerate(self.text):
            key_char = key[i % klen]
            cmap = self.table.get_map(key_char, decrypt=decrypt)
            result.append(cmap.get(char, char))

        return result

    def encrypt(self) -> List[str]:
        return self._transform(decrypt=False)

    def decrypt(self) -> List[str]:
        return self._transform(decrypt=True)
