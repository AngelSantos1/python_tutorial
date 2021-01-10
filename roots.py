def f(x):
	return x**3 - 6*(x**2) + 4*x + 12

def slope_f(x):
	#derivative with respect to 'x' 
	return 3*(x**2) - 12*x + 4


x = 0
e = 0.1

while abs(f(x)) > e: 
	print(str(x) + ": " + str(f(x)))
	x = x - f(x)/slope_f(x)

print("Done " + str(x) + ": " + str(f(x)))

# Use Newton's Method to find the roots of f(x)
# https://en.wikipedia.org/wiki/Newton%27s_method


