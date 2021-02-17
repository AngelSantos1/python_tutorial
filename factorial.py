import math 

a = 1
b = 1
if a == b:
    print ('1 through 10')

a = 11
while a > 1:
    a = a - 1
    print(a)


def factorial(a):
    b = a

    while b > 1: 
        b = b - 1
        a = a * b
    return a 

print(factorial(11))

def nchoosek(n,k):
    f = factorial(n)/(factorial(n-k)*factorial(k))
    return f

print(nchoosek(5,2))
   
print(math.cos(math.pi))
