import argparse
from pathlib import Path
from utils.load import load_yaml

def load_flag_config(cipher: str) -> dict:
    path = Path(__file__).parent / "config" / f"{cipher}.yaml"
    return load_yaml(path)

def load_all_cipher_configs(config_dir: Path) -> dict:
    ciphers = [
        p.stem for p in config_dir.glob("*.yaml")
        if p.stem not in ("default",)
    ]
    cipher_configs = {cipher: load_flag_config(cipher) for cipher in ciphers}
    return cipher_configs

def add_cipher_to_operation(op_parser, cipher, flags):
    cipher_parser = op_parser.add_parser(cipher)
    cipher_parser.add_argument("--text", required=True)
    for flag in flags:
        kwargs = {"required": flag.get("required", False)}
        if flag.get("default") is not None:
            kwargs["default"] = flag["default"]
        if flag["type"] == "int":
            kwargs["type"] = int
        elif flag["type"] == "str":
            kwargs["type"] = str
        cipher_parser.add_argument(flag["name"], **kwargs)

def add_operation(parser, op_name: str, cipher_configs: dict):
    op_parser = parser.add_parser(op_name)
    cipher_parsers = op_parser.add_subparsers(dest="cipher", required=True)
    for cipher, config in cipher_configs.items():
        if op_name not in config:
            continue
        add_cipher_to_operation(cipher_parsers, cipher, config[op_name])

def build_parser():
    parser = argparse.ArgumentParser(
        description="CryptoTractatus CLI – classical cipher toolkit"
    )
    operations = parser.add_subparsers(dest="operation", required=True)
    config_dir = Path(__file__).parent / "config"
    cipher_configs = load_all_cipher_configs(config_dir)
    all_ops = {op for cfg in cipher_configs.values() for op in cfg}
    for op_name in sorted(all_ops):
        add_operation(operations, op_name, cipher_configs)
    return parser
