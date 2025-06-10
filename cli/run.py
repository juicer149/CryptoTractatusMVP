import sys
import inquirer
from pathlib import Path

from cli.dispatch import dispatch
from cli.parser import build_parser
import cli.commands.caesar
import cli.commands.rot
import cli.commands.mono
import cli.commands.keywordmono


def get_available_ciphers():
    config_dir = Path(__file__).parent / "config"
    return [
        p.stem for p in config_dir.glob("*.yaml")
        if p.stem not in ("default",)
    ]

def run_interactive():
    parser = build_parser()
    cipher_choices = get_available_ciphers()
    op_choices = ["encrypt", "decrypt"]

    op = inquirer.list_input("Vad vill du göra?", choices=op_choices)
    cipher = inquirer.list_input("Vilken cipher?", choices=cipher_choices)

    # Dynamiskt fråga efter parametrar som krävs enligt YAML
    config_dir = Path(__file__).parent / "config"
    from utils.load import load_yaml
    cipher_config = load_yaml(config_dir / f"{cipher}.yaml")
    flags = cipher_config[op]

    questions = []
    for flag in flags:
        if flag["type"] == "int":
            questions.append(inquirer.Text(flag["name"].strip("-"), message=flag["name"] + " (int)"))
        else:
            questions.append(inquirer.Text(flag["name"].strip("-"), message=flag["name"]))
    questions.append(inquirer.Text("text", message="Text att transformera"))

    answers = inquirer.prompt(questions)
    if answers is None:
        print("Avbruten av användaren eller ingen input. Avslutar.")
        return

    sys_argv = [
        sys.argv[0],
        op,
        cipher,
        "--text", answers.pop("text")
    ]
    for flag in flags:
        val = answers.get(flag["name"].strip("-"))
        if val is not None:
            sys_argv.extend([flag["name"], str(val)])

    args = parser.parse_args(sys_argv[1:])
    result = dispatch(args)
    print("\nResultat:", "".join(result))

if __name__ == "__main__":
    run_interactive()
