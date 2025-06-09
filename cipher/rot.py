# ciphers/rot_cipher.py
from dataclasses import dataclass
from typing import List

from cipher.base import CipherBit
from cipher.charmap import CharMap
from utils.tools import rotate
from utils.quick import rot_text


@dataclass(kw_only=True)
class RotCipher(CipherBit):
    """
    Classic ROT (Caesar) cipher implementation.

    Args:
        shift (int): The number of positions to shift each character in the alphabet.
        fast (bool): If True, uses a faster method for transformations
    """
    shift: int

    def __post_init__(self):
        super().__post_init__()

    def _transform(self, direction: int) -> List[str]:
        """
        Applies the ROT transformation to the text.

        Args:
            direction (int): 1 for encryption, -1 for decryption.
        Returns:
            List[str]: The transformed text as a list of strings.
        """
        if self.fast:
            return list(rot_text("".join(self.text), direction * self.shift, self.alphabet))

        rotated = rotate(self.alphabet, -direction * self.shift)

        if direction == 1:
            mapping = CharMap.from_lists(self.alphabet, rotated)
        else:
            mapping = CharMap.from_lists(rotated, self.alphabet)

        return mapping(self.text)

    def encrypt(self) -> List[str]:
        return self._transform(1)

    def decrypt(self) -> List[str]:
        return self._transform(-1)
