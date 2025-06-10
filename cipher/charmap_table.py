from dataclasses import dataclass
from typing import List, Dict

from utils.tools import rotate, get_ascii_alphabet
from utils.alphabet_loader import load_alphabet
from cipher.interfaces import CipherTable
from pathlib import Path

@dataclass
class CharmapTable(CipherTable):
    _base_alphabet: List[str]
    _default_keyword: str
    forward_maps: Dict[str, Dict[str, str]]
    reverse_maps: Dict[str, Dict[str, str]]
    source: str  # e.g., "yaml:config/alpha/en.yaml", "ascii_fallback"

    @property
    def base_alphabet(self) -> List[str]:
        return self._base_alphabet

    @property
    def default_keyword(self) -> str:
        return self._default_keyword

    @classmethod
    def from_config(cls, name: str = "en", fallback: bool = True) -> 'CharmapTable':
        """
        Attempt to load alphabet from YAML using logical name (e.g., 'en').
        Falls back to ASCII if loading fails (unless fallback=False).
        """
        try:
            # If name looks like a language key ("en"), convert to a Path for load_alphabet
            # If you want to support config paths, do Path("config/alpha") / f"{name}.yaml"
            config_path = Path("config/alpha") / f"{name}.yaml"
            alphabet = load_alphabet(config_path)
            source = f"yaml:{name}"
        except Exception as e:
            if not fallback:
                raise RuntimeError(f"Could not load alphabet from config '{name}': {e}")
            alphabet = get_ascii_alphabet()
            source = "ascii_fallback"
            print(f"[CharmapTable] WARNING: Fallback to ASCII due to: {e}")
        
        return cls.from_alphabet(alphabet, source=source)

    @classmethod
    def from_alphabet(cls, alphabet: List[str], source: str) -> 'CharmapTable':
        """
        Construct a CharmapTable from a given alphabet (list of chars).
        Generates forward and reverse substitution maps.
        """
        forward = {}
        reverse = {}
        for i, key in enumerate(alphabet):
            shifted = rotate(alphabet, -i)
            forward[key] = dict(zip(alphabet, shifted))
            reverse[key] = dict(zip(shifted, alphabet))
        
        return cls(
            _base_alphabet=alphabet,
            _default_keyword=alphabet[0],
            forward_maps=forward,
            reverse_maps=reverse,
            source=source
        )

    def get_map(self, key_char: str, decrypt: bool = False) -> Dict[str, str]:
        """
        Get substitution map for a specific key character, depending on mode.
        """
        maps = self.reverse_maps if decrypt else self.forward_maps
        return maps.get(key_char, {})


    @classmethod
    def from_plain_and_cipher_alphabet(cls, plain_alphabet: list, cipher_alphabet: list, source: str) -> 'CharmapTable':
        # Endast EN map, ingen rotation
        forward = {plain_char: cipher_char for plain_char, cipher_char in zip(plain_alphabet, cipher_alphabet)}
        reverse = {cipher_char: plain_char for plain_char, cipher_char in zip(plain_alphabet, cipher_alphabet)}
        # Vi använder forward_maps/reverse_maps med EN entry (t.ex. key_char=plain_alphabet[0]) för kompatibilitet
        key = plain_alphabet[0]
        return cls(
            _base_alphabet=plain_alphabet,
            _default_keyword=key,
            forward_maps={key: forward},
            reverse_maps={key: reverse},
            source=source
        )
