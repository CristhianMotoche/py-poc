import sys
import argparse
import inspect
from typing import get_type_hints

def generate_cli_from_function(func):
    def _gen_parser(args: list[str]):
        parser = argparse.ArgumentParser(prog=func.__name__)
        hints = get_type_hints(func)
        sig = inspect.signature(func)

        for param_name, param in sig.parameters.items():
            param_type = hints.get(param_name, str)  # Default to str if no type hint
            arg_type = {
                int: int,
                bool: lambda x: x.lower() in ("yes", "true", "1"),
                str: str
            }.get(param_type, str)

            # If the parameter has a default value, make it optional
            if param.default is not param.empty:
                parser.add_argument(f"--{param_name}", type=arg_type, default=param.default)
            else:
                parser.add_argument(param_name, type=arg_type)

        return func(**vars(parser.parse_args(args)))
    return _gen_parser


@generate_cli_from_function
def example_command(name: str, age: int, active: bool = False):
    print(f"Name: {name}, Age: {age}, Active: {active}")


if __name__ == "__main__":
    example_command(sys.argv[1:])
