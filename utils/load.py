import yaml
import json
from pathlib import Path
from typing import Any


def load_yaml(path: Path) -> Any:
    """
    Load a YAML file and return its contents as Python data.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path) -> Any:
    """
    Load a JSON file and return its contents as Python data.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

