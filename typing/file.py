def headline(
    text,     # type: int
    align=True, # type: bool
):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline("python type checking"))
import math
# reveal_type(math.pi)
a = 100
print(headline("use mypy"))
print(__annotations__)
# reveal_locals()
