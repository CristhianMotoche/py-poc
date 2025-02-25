import argparse
import inspect
from typing import get_type_hints

def example_command(name: str, age: int, active: bool = False):
    """Example command function."""
    print(f"Name: {name}, Age: {age}, Active: {active}")

def generate_cli_from_function(func):
    parser = argparse.ArgumentParser(prog=func.__name__)
    hints = get_type_hints(func)
    sig = inspect.signature(func)

    for param_name, param in sig.parameters.items():
        param_type = hints.get(param_name, str)  # Default to str if no type hint
        arg_type = {int: int, bool: lambda x: x.lower() in ("yes", "true", "1"), str: str}.get(param_type, str)

        # If the parameter has a default value, make it optional
        if param.default is not param.empty:
            parser.add_argument(f"--{param_name}", type=arg_type, default=param.default)
        else:
            parser.add_argument(param_name, type=arg_type)

    return parser

# Generate parser and simulate CLI input
parser = generate_cli_from_function(example_command)
args = parser.parse_args(["John", "30", "--active", "true"])

# Call function with parsed arguments
example_command(**vars(args))
