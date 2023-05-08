from __future__ import annotations
# def substract(a: int, b: int) -> int:
#     return a - b
#
#
# def add(a: str, b: str) -> str:
#     return a + b
#
#
# add(10, '19')
#
# substract(10, '1')
#

class Counter:
    def __init__(self) -> None:
        self.value = 0

    def add(self, offset: int) -> None:
        self.value += offset

    def get(self) -> int:
        return self.value


counter = Counter()
counter.add(10)


def combine(func, value):
    assert len(value) > 0

    result = value[0]
    for next_value in value[1:]:
        result = func(result, next_value)

    return result


def add(a, b):
    return a + b


inputs = [1, 2, 3, 4 + 1j]

result = combine(add, inputs)

# assert result == 10

from typing import Callable, List, TypeVar

Value = TypeVar("Value")

Func = Callable[[Value, Value], Value]


def combine(func: Func, values: List[Value]) -> Value:
    assert len(values) > 0

    result = values[0]
    for next_value in values[1:]:
        result = func(result, next_value)

    return result


Real = TypeVar("Real", int, float)


def add(a: Real, b: Real) -> Real:
    return a + b


inputs = [1, 2, 3, 4 + 1j]

result = combine(add, inputs)


class FirstClass:
    def __init__(self, value: SecondClass) -> None:
        self.value = value


class SecondClass:
    def __init__(self, value: int) -> None:
        self.value = value


second = SecondClass(5)
print(second.value)
first = FirstClass(second)
