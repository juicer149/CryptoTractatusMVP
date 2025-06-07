from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).parent / "default.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)

def get_default_lang():
    return CONFIG.get("lang", "en")

def is_fast_mode_enabled():
    return CONFIG.get("fast_mode", True)

