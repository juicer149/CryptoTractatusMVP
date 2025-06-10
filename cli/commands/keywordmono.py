from cli.registry import register_command
from .mono_helpers import run_mono_variant

@register_command("encrypt", "keywordmono")
def keywordmono_encrypt(args):
    return run_mono_variant(args, mode="encrypt", variant="keywordmono")

@register_command("decrypt", "keywordmono")
def keywordmono_decrypt(args):
    return run_mono_variant(args, mode="decrypt", variant="keywordmono")
