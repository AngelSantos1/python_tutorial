#9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34


#index = 0
#fib = 0 
#temp = 1

#fib = temp

#while index < 50:
#	fib = fib + temp
#	print(fib, temp)
#	temp = temp + fib
	
#index = index + 1


x , y = 0,1

while y < 50:
    print(y)
    x , y = y, x + y


#y , x + y

