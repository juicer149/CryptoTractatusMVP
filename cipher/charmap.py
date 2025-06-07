# mapping/char_map.py

from dataclasses import dataclass
from typing import Dict, List, Iterable, Callable, Iterator, cast

from utils.errors import MappingLengthMismatchError
from utils.tools import zip_to_dict


@dataclass(frozen=True)
class CharMap:
    """
    Represents a simple character substitution map with a default fallback for unknown characters.
    
    Attributes:
        _mapping (Dict[str, str]): Internal character-to-character mapping.
        fallback (str): Character to use if lookup key is not found.
    """
    _mapping: Dict[str, str]
    fallback: str = "?"

    @classmethod
    def from_lists(
        cls,
        keys: Iterable[str],
        values: Iterable[str],
        fallback: str = "?"
    ) -> 'CharMap':
        """
        Construct a CharMap from two lists of equal length.

        Args:
            keys (Iterable[str]): Characters to be mapped from.
            values (Iterable[str]): Characters to be mapped to.
            fallback (str): Fallback character for unmapped lookups.

        Returns:
            CharMap: A new character map instance.

        Raises:
            MappingLengthMismatchError: If the input sequences differ in length.
        """
        
        mapping = zip_to_dict(list(keys), list(values), warn=False)
        
        if any(not isinstance(v, str) for v in mapping.values()):
            raise MappingLengthMismatchError("Keys and values must have the same length.")

        return cls(_mapping=cast(Dict[str, str], mapping), fallback=fallback)

    @classmethod
    def from_generator(
        cls,
        base: Iterable[str],
        generator: Callable[[Iterable[str], int], Iterator[Iterable[str]]],
        step: int = 1,
        #fallback: str = "?"
    ) -> Dict[str, List[str]]:
        """
        Generate a dictionary of character-to-sequence mappings using a transformation generator.

        This is useful in polyalphabetic ciphers like Vigenère, where each base character maps
        to a rotated alphabet or similar structure.

        Args:
            base (Iterable[str]): The base characters to generate mappings for.
            generator (Callable): A generator function yielding transformations of the base.
            step (int): Optional parameter passed to the generator.
            fallback (str): Not used in this context, included for interface symmetry.

        Returns:
            Dict[str, List[str]]: A dictionary mapping each character to a sequence.
        """
        base = list(base)
        sequences = list(generator(base, step))
        return zip_to_dict(base, *[list(s) for s in sequences])

    def __getitem__(self, key: str) -> str:
        """Return the mapped value or fallback if key is not found."""
        return self._mapping.get(key, self.fallback)

    def __call__(self, chars: Iterable[str]) -> List[str]:
        """Apply the mapping to an iterable of characters."""
        return [self[c] for c in chars]

    def as_dict(self) -> Dict[str, str]:
        """Return a shallow copy of the internal mapping dictionary."""
        return self._mapping.copy()

