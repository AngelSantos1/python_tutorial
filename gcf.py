def gcf(x,y):
	while (y):
		x,y = y, x % y
	return(x)

gcf = gcf(200, 100)

print(gcf)
	
