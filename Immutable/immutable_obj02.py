# Неизменяемый объект. 
from collections import namedtuple

# Core

class Field( namedtuple("Field", ["name", "value", "type"]) ):
    def __new__(cls, name, value, type_):
        if not isinstance(value, type_):
            raise ValueError("Value {} / type error {}".format(value, type_ ))
        return super().__new__(cls, name, value, type_)


class BaseNamedTuple:

    def __new__(cls, *args, **kwargs):
        fields = cls.__annotations__.keys()
        # print([cls.__name__ for cls in BaseNamedTuple.__subclasses__()])
        obj = super().__new__(cls)
        
        for key, val in kwargs.items():
            kwargs[key] = Field(name=key, value=val, type_=cls.__annotations__[key])

        return namedtuple( obj.__class__.__name__ , fields)(**kwargs)

# Example

class IChild(BaseNamedTuple):
    name: str
    year: int

class ICar(BaseNamedTuple):
    name: str
    year: int
    price: float


artem = IChild( name="Artem", year=8 )
print(artem.year.name)
print(artem.year.value)
print(artem.year.type)
print("=========")

params = {
    "price":140000.00,   
    "name":"Vaz 2114",
    "year":2010,
}

car = ICar(**params)
print(car.year.name)
print(car.year.value)
print(car.year.type)

# import pdb;pdb.set_trace()
# prit()
# test = Child(name="Artem", year=8,)