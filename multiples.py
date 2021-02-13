#10. Write a Python program which iterates the integers from 1 to 50. 
#For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#Sample Output :
#fizzbuzz

limit = 0

while limit < 51:
	if limit % 3 == 0 and limit % 5 == 0:
		print("fizzbuzz", limit)
	elif limit % 3 == 0:
		print("fizz", limit)
	elif limit % 5 == 0:
		print("buzz", limit)
	else:
		print(limit)
	limit = limit + 1
