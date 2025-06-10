from cli.registry import register_command
from .mono_helpers import run_mono_variant

@register_command("encrypt", "rot")
def rot_encrypt(args):
    return run_mono_variant(args, mode="encrypt", variant="rot")

@register_command("decrypt", "rot")
def rot_decrypt(args):
    return run_mono_variant(args, mode="decrypt", variant="rot")
