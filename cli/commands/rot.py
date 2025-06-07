# cli/commands/rot.py
"""
ROT cipher command handlers for the CLI.

This module registers `encrypt` and `decrypt` operations for the ROT cipher
via the decorator-based command registry. It builds the cipher from CLI args
and supports fast fallback logic via configuration.
"""

from cipher.rot import RotCipher
from language.tools import load_unicode_alphabet
from cli.registry import register_command
from cli.config.settings import get_default_lang, is_fast_mode_enabled

def _build_rot_cipher(args, mode: str):
    """
    Constructs a RotCipher instance from CLI arguments.

    Handles:
    - Language-based default alphabet loading
    - Fast mode toggling via config
    - Dispatch based on operation mode

    Args:
        args: Parsed CLI arguments.
        mode (str): Operation mode, e.g., "encrypt" or "decrypt".

    Returns:
        List[str]: Transformed characters after encryption or decryption.
    """
    lang = args.lang or get_default_lang()
    alphabet = list(args.alphabet) if args.alphabet else load_unicode_alphabet(lang)
    use_fast = args.alphabet is None and is_fast_mode_enabled()

    cipher = RotCipher(
        text=list(args.text),
        shift=args.shift,
        alphabet=alphabet,
        fast=use_fast
    )

    return cipher(mode=mode)


@register_command("encrypt", "rot")
def handle_rot_encrypt(args):
    """
    CLI handler for ROT encryption.

    Registered for: operation="encrypt", cipher="rot"
    """
    return _build_rot_cipher(args, mode="encrypt")


@register_command("decrypt", "rot")
def handle_rot_decrypt(args):
    """
    CLI handler for ROT decryption.

    Registered for: operation="decrypt", cipher="rot"
    """
    return _build_rot_cipher(args, mode="decrypt")

