# Design a function "factor(x)" that returns the list of prime factors for x. 
# Likely, you'll want to use the function from the previous problem.
# For example, factor(20) would return [2, 2, 5] and factor(51) would return [3, 17].
# 
#get all the primes from 0 to n/2
# test each prime p to see if n is divisible by p
# if n is not divisible by p, then move on to the next prime
# if n is divisible by p, add p to the list of factors and set n to n/p

# a / b = x 
# 10 / 4 = 2.5 or 2 remainder 2

# 10 % 4 = 2

# a is divisble by b if the remainer is 0 

# a % b == 0 

from prime_number import prime 

#a / b = x



n = 100  
i = 0
l = []

p = prime(int(n/2))
# p = [2,3,5,7,11,13,17,19...]
# p is the variable that contains the list returned by the prime function
#print(p)

while i < len(p):  
	# myprime = p[i] .grab a single prime number from 
	if n % p[i] == 0: 
		l.append(p[i])
		n = n/p[i]
	else: 
		i = i + 1

print(l)
