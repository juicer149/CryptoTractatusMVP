"""
Registry and decorator for mapping CLI operations and ciphers to their handler functions.
"""

COMMAND_REGISTRY = {}

def register_command(operation, cipher):
    """
    Decorator to register a command handler for a given operation and cipher.

    Args:
        operation (str): The CLI operation, e.g., "encrypt", "decrypt".
        cipher (str): The cipher name, e.g., "rot", "vigenere".

    Returns:
        Callable: The decorated handler function.
    """
    def decorator(fn):
        COMMAND_REGISTRY.setdefault(operation, {})[cipher] = fn
        return fn
    return decorator
