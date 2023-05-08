# -*- coding: utf-8 -*-
from dataclasses import dataclass, replace, astuple, asdict


@dataclass(order=True, frozen=True)
class Color:
    red: int
    blue: int
    green: int


class Color2:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green


c = Color(1, 2, 3)
d = Color(1, 2, 3)
sorted([c, d])
c = replace(c, red=4)
c_tuple = astuple(c)
d = Color2(1, 2, 3)

c_annotations = Color.__annotations__
print(c_annotations)
import sys

mem = sys.getsizeof(c) + sys.getsizeof(vars(c))
print(mem)
mem2 = sys.getsizeof(d) + sys.getsizeof(vars(d))
print(mem2)
print(asdict(c))


####### dataclasses #########

# creating a dict from a dataclass args
from dataclasses import asdict

print("class_dict", asdict(c))

# creating a tuple from a dataclass args
from dataclasses import astuple

print("class_tuple", astuple(c))

# creating a new dataclass instance from an existing one
from dataclasses import replace

c2 = replace(c, red=3)
print("new_object", c2)

# fetching all annotations from a dataclass
print("Annotations", c.__annotations__)

# extracting all fields from a dataclass
from dataclasses import fields

print(" ** Fields ** ")
class_fields = fields(c)
for field in class_fields:
    print(field)

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(order=True, frozen=True)
class Employee:
    emp_id: int = field()
    name: str = field()
    salary: float = field(hash=False, repr=False, metadata={"units": "USD"})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, access_id):
        self.viewed_by.append((access_id, datetime.now()))


from typing import NamedTuple


class Point2(NamedTuple):
    x: int
    y: int


d = Point2(1, 2)


####### dataclasses #########

# creating a dict from object attributes
print("class_dict", d._asdict())
## Output -> class_dict {'x': 1, 'y': 2}

# creating a tuple from a object attributes
print("class_tuple", tuple(d))
## Output -> class_tuple (1, 2)

# creating a new class instance from an existing one
d2 = d._replace(x=3)
print("new_object", d2)
## Output -> new_object Point2(x=3, y=2)

# fetching all annotations from a instance
print("Annotations", d.__annotations__)
## Output -> Annotations {'x': <class 'int'>, 'y': <class 'int'>}


x_co, y_co = d2


data_dict = {d: 100}

for i in d:
    print(i)


#%%
@dataclass(order=True, frozen=True)
class Point:
    x: int
    y: int = 10


c = Point(1, 2)
d = Point(-1, 2)

print(sorted([c, d]))

print(c == d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)

print(d)
d = replace(c, x=3)
{d: "100"}
# order=True will implement __lt__, __le__, __gt__, __ge__ methods


#%%
from dataclasses import dataclass, field, fields
from datetime import datetime


@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int = field()
    name: str = field()
    gender: str = field()
    salary: int = field(hash=False, repr=False, metadata={"units": "USD"})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, access_id):
        self.viewed_by.append((access_id, datetime.now()))


e = Employee(1, "John", "M", 1000, 30)
f = Employee(2, "Jane", "F", 2000, 25)
e.access("Manager1")
e.access("Manager2")

f.access("Manager1")
f.access("Manager2")

result = sorted([e, f])
print(fields(e)[3].metadata)


# Inheritance in dataclasses

from dataclasses import dataclass, asdict


class Serialize:
    def __init__(self, kwargs):
        self.kwargs = kwargs

    def serialize(self):
        import json

        return json.dumps(self.kwargs)


@dataclass
class Point(Serialize):
    x: int
    y: int

    def __post_init__(self):
        super().__init__(asdict(self))


c = Point(1, 2)
print(c.serialize())
