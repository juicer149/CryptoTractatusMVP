from abc import ABC, abstractmethod
from typing import Dict, List

class CipherTable(ABC):
    """
    Interface for character mapping tables used in substitution ciphers.

    Implementations must provide forward and reverse character maps for each key.
    This abstraction allows Vigenère, Caesar, homophonic and other ciphers to share
    the same transformation logic.
    """

    @abstractmethod
    def get_map(self, key_char: str, decrypt: bool = False) -> Dict[str, str]:
        """
        Return the character substitution map for a given key character.
        
        Args:
            key_char (str): Character used to select the row of the mapping table.
            decrypt (bool): If True, returns reverse map; else forward map.

        Returns:
            Dict[str, str]: Mapping of characters (plain -> cipher or vice versa).
        """
        pass

    @property
    @abstractmethod
    def base_alphabet(self) -> List[str]:
        """
        The reference alphabet on which this table is based.
        """
        pass

    @property
    @abstractmethod
    def default_keyword(self) -> str:
        """
        Default key character used when no specific key is provided.
        """
        pass
