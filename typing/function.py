import numpy as np # type: ignore
from typing import Tuple, NoReturn, Any, Callable


def function(a:str, b:int, c:str) -> None:
    print(a, b, c)

def f2(fn: Callable[[str, int, str], None], *args:Tuple[str, int, str]) -> None:
    fn(*args)

print(f2(function, ("1",2,"3")))
