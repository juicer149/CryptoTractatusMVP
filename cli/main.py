# Main CLI entry point for CryptoTractatus.

from cli.parser import build_parser
from cli.dispatch import dispatch

# Import ALL commands to ensure they are registered!
import cli.commands.caesar
import cli.commands.rot
import cli.commands.keywordmono
import cli.commands.mono
import cli.commands.pipeline
import cli.commands.vigenere

def main():
    parser = build_parser()
    args = parser.parse_args()
    result = dispatch(args)
    print("".join(result))

if __name__ == "__main__":
    main()
