#Unlimited positional arguments (*args)
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,3,4,2))

#Arbitary number of keyword arguments (**kwargs)

def calculate(**kwargs):
    #print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #
    print(kwargs["add"])

calculate(add=3, multiply=5)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# so, n=2 is added to 3 and then multiplied by 5 what gives us 25
calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        #notice if you would use self.make = kwargs["make"] you get error during class initialising
        self.model = kwargs.get("model")

my_car = Car()
my_car1 = Car(make="Nissan")
my_car2 = Car(make="Nissan", model="GT-I")

print(my_car.model)
print(my_car.make)
print(my_car1.model)
print(my_car1.make)
print(my_car2.model)
print(my_car2.make)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
# and the output is:    4 (7, 3, 0) {'x': 10, 'y': 64} #one variable, args generate tuple and kwargs dictionary