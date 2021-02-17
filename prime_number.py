def prime(n):

	l = [0]*n
	p = 2
	 
	while p < n:
		if l[p] == 0: 
			q = 2*p
			while q < n:
				l[q] = 1
				q = q + p
		p = p + 1

	result = []

	i = 2
	while i < n:
		if l[i] == 0:
			result.append(i) 
		i = i + 1
	return result

#print(prime(200))
