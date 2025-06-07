# cli/main.py
# Main CLI entry point for CryptoTractatus.

from cli.parser import build_parser
from cli.dispatch import dispatch

import cli.commands.rot

def main():
    parser = build_parser()
    args = parser.parse_args()
    result = dispatch(args)
    print("".join(result))

if __name__ == "__main__":
    main()
