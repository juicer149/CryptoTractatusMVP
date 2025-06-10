from cli.registry import COMMAND_REGISTRY
from utils.errors import UnknownCommandError

def dispatch(args):
    """
    Dispatch parsed CLI arguments to the registered cipher handler.

    Raises:
        UnknownCommandError: If no matching handler is found.
    """
    try:
        return COMMAND_REGISTRY[args.operation][args.cipher](args)
    except KeyError:
        raise UnknownCommandError(args.operation, args.cipher)
