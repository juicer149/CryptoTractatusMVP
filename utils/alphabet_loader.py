from pathlib import Path
from typing import List, Optional, Union

from utils.load import load_yaml
from utils.tools import get_ascii_alphabet

def load_alphabet_from_yaml(path: Path) -> List[str]:
    if not path or not path.exists():
        raise FileNotFoundError(f"YAML alphabet file not found: {path}")
    data = load_yaml(path)
    if isinstance(data, dict) and "alphabet" in data:
        return list(data["alphabet"])
    elif isinstance(data, str):
        return list(data)
    elif isinstance(data, list):
        return data
    elif isinstance(data, dict) and "range" in data:
        # Stöd för range-baserad YAML, t.ex. en.yaml/sv.yaml
        alphabet = []
        for r in data["range"]:
            start = int(r["start"])
            end = int(r["end"])
            alphabet.extend([chr(i) for i in range(start, end)])
        return alphabet
    else:
        raise ValueError(f"Invalid format in alphabet file: {path}")

def load_alphabet(lang_or_path: Optional[Union[str, Path]] = None, fallback: bool = True) -> List[str]:
    """
    Förbättrad robusthet:
    1. Om sträng: tolka som språk, sök i language/alphabets/<lang>.yaml
    2. Om Path: använd direkt
    3. Om None: fallback till ASCII
    """
    path = None
    if isinstance(lang_or_path, str):
        # Sök filen i projektets struktur
        path = (Path(__file__).parent.parent / "language" / "alphabets" / f"{lang_or_path}.yaml").resolve()
    elif isinstance(lang_or_path, Path):
        path = lang_or_path.resolve() if lang_or_path else None

    try:
        if path:
            return load_alphabet_from_yaml(path)
        else:
            raise FileNotFoundError("No alphabet path or language specified.")
    except Exception as e:
        if not fallback:
            raise
        print(f"[Alphabet] WARNING: Falling back to ASCII: {e}")
        return get_ascii_alphabet()
