# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
    
    
# print(add(6,4,4,5))

# def calculate(n, **kwargs):
#     n *= kwargs["multiply"]
#     n += kwargs["add"]
#     print(n)
    
    
# calculate(2, add=4, multiply=7)


class Car:
    
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car = Car(model="GTR")

print(my_car.make)