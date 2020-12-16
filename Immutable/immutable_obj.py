# Неизменяемый объект.
from collections import namedtuple


class Field( namedtuple("Field", ["name", "value", "type"]) ):
    def __new__(cls, name, value, type_):
        if not isinstance(value, type_):
            raise ValueError("Value {} / type error {}".format(value, type_ ))
        return super().__new__(cls, name, value, type_)

class Car( namedtuple("Car", ["brand", "year", "price"]) ):
    pass


audi = Car(
    brand=Field("brand", "audi", str),
    year= Field("year", 2015, int),
    price=Field("price", 2000000.00, float)
)

print( audi.brand.name )
print( audi.brand.value )
print( audi.brand.type )
# =============
# brand
# audi
# <class 'str'>

