#Greatest Common Factor
#Design a function "gcf(x, y)" that returns the greatest common factor 
# between x and y using the euclidean algorithm.

def gcf(x,y):
	while(y):
		x, y = y, x % y
	return x

gcf = gcf(300, 400)
print('The GCF is', gcf)


def gcf(x,y):
	while (x):
		x , y = y, x % y
	return x

gcf = gcf(300,400)
print(gcf)

	
