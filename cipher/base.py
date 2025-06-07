from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

from utils.validators import ensure_not_empty


@dataclass
class CipherBit(ABC):
    """
    Abstract base class for cipher bits.
    """

    text: List[str]
    alphabet: List[str]
    fast: bool = False

    def __post_init__(self):
        self.text = list(self.text)
        self.alphabet = list(self.alphabet)

        ensure_not_empty(self.text, "Text must not be empty.")
        ensure_not_empty(self.alphabet, "Alphabet must not be empty.")

    
    def __call__(self, mode: str = "encrypt") -> List[str]:
        return self.encrypt() if mode == "encrypt" else self.decrypt()


    @abstractmethod
    def encrypt(self) -> List[str]:
        """
        Encrypt the text using the cipher's algorithm.
        Returns a list of encrypted characters.
        """
        pass

    @abstractmethod
    def decrypt(self) -> List[str]:
        """
        Decrypt the text using the cipher's algorithm.
        Returns a list of decrypted characters.
        """
        pass


