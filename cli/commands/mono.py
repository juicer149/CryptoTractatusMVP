from cli.registry import register_command
from .mono_helpers import run_mono_variant

@register_command("encrypt", "mono")
def mono_encrypt(args):
    return run_mono_variant(args, mode="encrypt", variant="mono")

@register_command("decrypt", "mono")
def mono_decrypt(args):
    return run_mono_variant(args, mode="decrypt", variant="mono")
