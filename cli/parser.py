# cli/parser.py

import argparse
from pathlib import Path
from utils.load import load_yaml


def load_flag_config(cipher: str) -> dict:
    """
    Load CLI flag configuration for a specific cipher from a YAML file.

    Args:
        cipher (str): The name of the cipher (e.g., "caesar", "vigenere").

    Returns:
        dict: Dictonary with CLI flags grouped by operation, (encrypt, decrypt, etc.).
    """
    path = Path(__file__).parent / "config" / f"{cipher}.yaml"
    return load_yaml(path)


def load_all_cipher_configs(config_dir: Path) -> dict:
    """
    Load YAML configuration files for all ciphers in the specified directory.

    Args:
        config_dir (Path): Directory containing cipher YAML files.

    Returns:
        dict: A mapping from cipher names to their configuration dictionaries.
    """
    # Exkludera default.yaml och eventuella andra icke-cipher-YAML
    ciphers = [
        p.stem for p in config_dir.glob("*.yaml")
        if p.stem not in ("default",)
    ]
    cipher_configs = {cipher: load_flag_config(cipher) for cipher in ciphers}
    return cipher_configs


def add_cipher_to_operation(op_parser, cipher, flags):
    """
    Add a cipher as a subparser under a given operation with its configured flags.

    Args:
        op_parser: The subparser object for an operation (e.g., encrypt).
        cipher (str): Name of the cipher (e.g., "rot").
        flags (list): List of flag specifications from the YAML config.
    """
    cipher_parser = op_parser.add_parser(cipher)
    cipher_parser.add_argument("--text", required=True)

    for flag in flags:
        kwargs = {"required": flag.get("required", False)}
        if flag["type"] == "int":
            kwargs["type"] = int
        elif flag["type"] == "str":
            kwargs["type"] = str

        cipher_parser.add_argument(flag["name"], **kwargs)


def add_operation(parser, op_name: str, cipher_configs: dict):
    """
    Add an operation (encrypt, decrypt, analyze, etc.) and all applicable ciphers.

    Args:
        parser: The main argparse parser.
        op_name (str): The operation name (e.g., "encrypt").
        cipher_configs (dict): Mapping of cipher names to their CLI flag configs.
    """
    op_parser = parser.add_parser(op_name)
    cipher_parsers = op_parser.add_subparsers(dest="cipher", required=True)

    for cipher, config in cipher_configs.items():
        if op_name not in config:
            continue
        add_cipher_to_operation(cipher_parsers, cipher, config[op_name])


def build_parser():
    """
    Build the complete CLI argument parser by loading configs and attaching operations/ciphers.

    Returns:
        argparse.ArgumentParser: Fully constructed parser ready for CLI use.
    """
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
