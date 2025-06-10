from cli.registry import register_command
from .mono_helpers import run_mono_variant

@register_command("encrypt", "caesar")
def caesar_encrypt(args):
    return run_mono_variant(args, mode="encrypt", variant="caesar")

@register_command("decrypt", "caesar")
def caesar_decrypt(args):
    return run_mono_variant(args, mode="decrypt", variant="caesar")
