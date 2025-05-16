from typing import Annotated, Type, get_type_hints

class Foo:
    x: Annotated[int, 'hello', 'wolrd']

def print_meta(cl: Type):
    for k, v in get_type_hints(cl, include_extras=True).items():
        print(k, ' says: ', v.__metadata__)

print_meta(Foo)
