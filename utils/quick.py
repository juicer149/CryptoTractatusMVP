# utils/quick.py

"""
Quick transformation utilities for CLI defaults and minimal pipelines.
[...]
"""

from typing import List, Optional

from utils.tools import rotate
from utils.validators import ensure_not_empty
from language.tools import load_unicode_alphabet


def rot_text(
    text: str,
    shift: int,
    alphabet: Optional[List[str]] = None,
    lang: str = "en"
) -> str:
    """
    Fast Caesar-style rotation of a string using a given alphabet.
    If no alphabet is provided, defaults to Unicode-based alphabet via language config.

    Args:
        text (str): Input string to transform.
        shift (int): Rotation amount.
        alphabet (Optional[List[str]]): Custom alphabet to use. If None, load default.
        lang (str): Language code for default alphabet (used if alphabet is None).

    Returns:
        str: Transformed string with shifted characters.
    """
    ensure_not_empty(text)

    if alphabet is None:
        alphabet = load_unicode_alphabet(lang)

    ensure_not_empty(alphabet)

    rotated = rotate(alphabet, -shift)
    index_map = {char: idx for idx, char in enumerate(alphabet)}

    return ''.join(
        rotated[index_map[char]] if char in index_map else char for char in text
    )

