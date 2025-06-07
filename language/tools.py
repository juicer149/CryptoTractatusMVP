"""
Language-specific tools for Unicode-based alphabet configuration.

Provides:
- Loading of language-specific alphabets from YAML
- Fallback for Latin-based defaults (A–Z)
- Generation of YAML alphabet files using Unicode ranges + extras

Used in CLI defaults, cipher setup, and transformation logic.
"""

from typing import List, Dict, Optional
from pathlib import Path
from utils.load import load_yaml

ALPHABET_DIR = Path(__file__).parent / "alphabets"


def load_unicode_alphabet(lang: str = "en") -> List[str]:
    """
    Load an alphabet from YAML using a language code.

    Supports:
    - Unicode range: start & end
    - Extras: additional characters mapped to Unicode code points

    Args:
        lang (str): Language code (e.g. 'en', 'sv', 'el')

    Returns:
        List[str]: Alphabet as list of characters
    """
    path = ALPHABET_DIR / f"{lang.lower()}.yaml"
    if not path.exists():
        return basic_unicode_latin()

    config = load_yaml(path)
    alphabet = []

    if "range" in config:
        for r in config["range"]:
            alphabet.extend([chr(i) for i in range(r["start"], r["end"])])

    if "extras" in config and isinstance(config["extras"], dict):
        alphabet.extend([chr(cp) for cp in config["extras"].values()])

    return alphabet


def generate_unicode_yaml(
    name: str,
    start: int,
    end: int,
    extras: Optional[List[str]] = None,
    out_dir: Path = ALPHABET_DIR
) -> None:
    """
    Generate a YAML alphabet file with a Unicode range and optional extras.

    Args:
        name (str): Language name/code (used as filename)
        start (int): Start Unicode code point (inclusive)
        end (int): End Unicode code point (exclusive)
        extras (List[str]): Optional characters to include
        out_dir (Path): Directory to save YAML file
    """
    import yaml

    out_dir.mkdir(parents=True, exist_ok=True)
    filepath = out_dir / f"{name.lower()}.yaml"

    data: Dict = {
        "range": {
            "start": start,
            "end": end,
            "name": name
        }
    }

    if extras:
        data["extras"] = {char: ord(char) for char in extras}

    with open(filepath, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)

    print(f"[✓] Created alphabet YAML: {filepath}")


def basic_unicode_latin() -> List[str]:
    """
    Default fallback alphabet: A–Z (Unicode 65–90)

    Returns:
        List[str]: Uppercase Latin letters
    """
    return [chr(i) for i in range(65, 91)]

