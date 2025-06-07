# ciphers/rot_cipher.py

from dataclasses import dataclass
from typing import List

from cipher.base import CipherBit
from cipher.charmap import CharMap
from utils.tools import rotate
from utils.quick import rot_text


@dataclass(kw_only=True)
class RotCipher(CipherBit):
    shift: int

    def __post_init__(self):
        super().__post_init__()

    def encrypt(self) -> List[str]:
        # Fast fallback when alphabet is not given
        if self.fast:
            return list(rot_text("".join(self.text), self.shift, self.alphabet))
        rotated = rotate(self.alphabet, -self.shift)  
        mapping = CharMap.from_lists(self.alphabet, rotated)
        return mapping(self.text)

    def decrypt(self) -> List[str]:
        if self.fast:
            return list(rot_text("".join(self.text), -self.shift, self.alphabet))
        rotated = rotate(self.alphabet, -self.shift)
        mapping = CharMap.from_lists(rotated, self.alphabet)
        return mapping(self.text)

