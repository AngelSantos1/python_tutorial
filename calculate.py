#14. Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
#Sample Data : Python 3.2
#Expected Output :
#Letters 6
#Digits 2

s = input("Input a string: ")
d = 0 
l = 0
limit = 0

while len(s) > limit:
	if s[limit].isdigit():
		d = d + 1    
	elif s[limit].isalpha():
		l = l + 1
	#else:
	#	pass
	limit = limit + 1

print("Letters", l)
print("Digits", d)
#print(limit)	


#Tutor solution
#for c in s:
#    if c.isdigit():
#        d=d+1
#    elif c.isalpha():
#        l=l+1
#    else:
#        pass
#print("Letters", l)
#print("Digits", d)




#string = input("Calculate the number an digits of this string:")

#index = [string]
#len(string)
#digits = [0,1,2,3,4,5,6,7,8,9] 
#stop = 0
#" " = -1

#while index > stop:
#	stop = stop + 1


#print(index)

#print(string)

#print("\n")
