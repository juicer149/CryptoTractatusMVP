from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

from utils.validators import ensure_not_empty

@dataclass
class CipherBit(ABC):
    """
    Abstract base class for cipher components ("cipher bits").
    Each subclass must implement `encrypt()` and `decrypt()` methods.
    Attributes:
        text (List[str]): The input to be transformed.
        alphabet (List[str]): The working alphabet used for mapping.
        fast (bool): Optional performance hint for downstream implementations.
    """
    text: List[str]
    alphabet: List[str]
    fast: bool = False

    def __post_init__(self):
        """
        Normalize and validate inputs.
        Ensures that text and alphabet are both non-empty lists.
        """
        self.text = list(self.text)
        self.alphabet = list(self.alphabet)

        ensure_not_empty(self.text, "Text must not be empty.")
        ensure_not_empty(self.alphabet, "Alphabet must not be empty.")

    def __call__(self, mode: str = "encrypt") -> List[str]:
        """
        Enable instance to be called as a function:
        >>> cipher() == cipher.encrypt()
        >>> cipher("decrypt") == cipher.decrypt()
        """
        return self.encrypt() if mode == "encrypt" else self.decrypt()

    @abstractmethod
    def encrypt(self) -> List[str]:
        """
        Encrypt the text using the cipher's algorithm.
        Must return a list of encrypted characters.
        """
        pass

    @abstractmethod
    def decrypt(self) -> List[str]:
        """
        Decrypt the text using the cipher's algorithm.
        Must return a list of decrypted characters.
        """
        pass
