# tools.py – pure utility functions for character sequence manipulation

"""This module provides utility functions for character sequence manipulation.

All functions in this module are:
- Pure and deterministic
- Accept general iterables
- Return new list objects
- Do not raise exceptions for common input variants (e.g. empty iterables)
"""

from typing import Any, Dict, List, Union, Sequence 
import warnings
from collections.abc import Iterable


def rotate(sequence: Iterable[str], shift: int) -> list[str]:
    """
    Rotate a sequence of characters by a specified number of positions.

    Args:
        sequence (Iterable[str]): An iterable of individual characters.
        shift (int): The number of positions to rotate the sequence.
                     Positive values rotate to the right, negative values to the left.
                     For Caesar-style cipher logic (A → B), use a negative shift. 

    Returns:
        list[str]: A new list with the rotated characters.

    Example:
        >>> rotate('abcdef', 2)
        ['e', 'f', 'a', 'b', 'c', 'd']
        >>> rotate('abcdef', -2)
        ['c', 'd', 'e', 'f', 'a', 'b']
    """
    # Convert the sequence to a list to support indexing
    sequence = list(sequence)

    # Handle empty sequence to avoid ZeroDivisionError
    if not sequence:
        return []

    # Normalize the shift to avoid unnecessary full rotations
    shift %= len(sequence)  # Normalize shift to the length of the sequence

    return sequence[-shift:] + sequence[:-shift] if shift else sequence.copy()



def remove_duplicates(sequence: Iterable[str]) -> list[str]:
    """
    Remove duplicates from a sequence while preserving the order of first occurrences.

    Useful for reducing character sequences (e.g. keywords) before generating cipher mappings.

    Note:
        This function does not filter out non-letter characters.
        If used for cipher keywords, ensure to preprocess the input (e.g. with `str.isalpha`)
        before passing it to this function to avoid including unintended symbols.

    Args:
        sequence (Iterable[str]): An iterable of individual characters.

    Example:
        >>> remove_duplicates('secret')
        ['s', 'e', 'c', 'r', 't']
        >>> remove_duplicates("secret keyword") # Example with spaces
        ['s', 'e', 'c', 'r', 't', ' ', 'k', 'y', 'w', 'o', 'd']
    """
    return list(dict.fromkeys(sequence)) # Uses dict.fromkeys to make use of CPython's order-preserving nature of dictionaries.




def zip_to_dict(
    keys: Iterable[Any],
    *value_lists: Sequence[Any],
    warn: bool = True
) -> Dict[Any, Union[Any, List[Any]]]:
    """
    Zip keys with one or more value sequences into a dictionary.

    If a single value list is provided, each key maps to one value.
    If multiple lists are provided, each key maps to a list of values.

    Args:
        keys (Iterable[Any]): Keys to be used in the dictionary.
        *value_lists (Sequence[Any]): One or more sequences of values.
        warn (bool): Whether to warn when a value list is shorter than keys.

    Returns:
        dict[Any, Union[Any, List[Any]]]: Mapping of keys to values or lists of values.

    Example:
        >>> zip_to_dict(['A', 'B'], ['X', 'Y'])
        {'A': 'X', 'B': 'Y'}
        >>> zip_to_dict(['A', 'B'], ['X', 'Y'], [1, 2])
        {'A': ['X', 1], 'B': ['Y', 2]}
        >>> zip_to_dict(['A', 'B', 'C'], ['X', 'Y'])
        {'A': 'X', 'B': 'Y', 'C': None}
    """
    keys = list(keys)
    single = len(value_lists) == 1
    result = {}

    for i, key in enumerate(keys):
        values = []
        for vlist in value_lists:
            if i < len(vlist):
                values.append(vlist[i])
            else:
                if warn:
                    warnings.warn(f"Value list shorter than keys at index {i}")
                values.append(None)
        result[key] = values[0] if single else values

    return result
