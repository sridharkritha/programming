#! /usr/bin/python


# named function
def polynomial(x):
    return x**2 + 5*x + 4

print(polynomial(5))

# lambda function
print( (lambda x: x**2 + 5*x + 4) (5) )

add = lambda x,y: x + y

print(add(7,2))
