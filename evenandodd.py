#Write a Python program to count the number of even and odd numbers from a series of numbers. 
#Go to the editor
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4


#n = n % 2 

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0 
even = 0
odd = 0

while i < len(n):
	if n[i] % 2 == 0:
		even = even + 1
		#print("even")
	else:
		odd = odd + 1
		#print("odd") 
	i = i + 1 	
print("Even:", even)
print("Odd:", odd)


#print(n) 

#print(n%2)


# 5 / 2 = 2 Remainder 1 


#while 
#	stuff
