# def foo(*args):
#     return sum(args) / len(args)
# print(foo(10,20,40))
def foo1(*args):
     args = [x.upper() for x in args]
     return sorted(args)
print(foo1("snow","glacier","kupa"))