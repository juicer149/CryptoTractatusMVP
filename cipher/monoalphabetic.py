from dataclasses import dataclass
from typing import List

from cipher.base import CipherBit
from cipher.interfaces import CipherTable
from utils.validators import ensure_not_empty

@dataclass(kw_only=True)
class MonoalphabeticCipher(CipherBit):
    """
    A simple monoalphabetic substitution cipher.
    Uses a single substitution map derived from a CipherTable.
    """
    key_char: str
    table: CipherTable

    def __post_init__(self):
        super().__post_init__()
        if self.key_char not in self.table.base_alphabet:
            raise ValueError(f"Key character '{self.key_char}' not in table's alphabet.")
        ensure_not_empty(self.table.base_alphabet, "Cipher table alphabet must not be empty.")

    def _transform(self, decrypt: bool) -> List[str]:
        cmap = self.table.get_map(self.key_char, decrypt=decrypt)
        return [cmap.get(c, c) for c in self.text]

    def encrypt(self) -> List[str]:
        return self._transform(decrypt=False)

    def decrypt(self) -> List[str]:
        return self._transform(decrypt=True)
