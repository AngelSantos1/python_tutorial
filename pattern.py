#a = '*' 
#b = 0

#while b < 5: 
    #b = b + 1
    #print(a)
    #a = a + '*'

#a = '*'
#b = 0

#while b < 5:
    #b = b + 1
    #print(a)
    #a = a + '*'

x = 0
y = 0
r = 25
n = 2*r

while y < n:
    x = 0
    while x < n:
        if (x-r)**2 + (y-r)**2 < r**2: 
            print('*', end="")
        else: 
            print(' ', end="")
        x = x + 1
    print()
    y = y + 1

#r = x**2 + y**2
#a = '*'

#while x < r:
    #x = x + x 
    #print(a)
#while y < r:
    #y = y + y
    #print(a)


#b = 4**2 + 6**2 
#print(b)

#a = '*'
#x = 4#y = 6





# x**2 + y**2 < r**2
# print "my string", end="")


