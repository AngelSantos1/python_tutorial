"""
Write a Python program to find those numbers which are divisible by 7 
and multiple of 5, between 1500 and 2700 (both included). 
"""

i = 1500
l = []

while i < 2700:
	i = i + 1
	if (i%7==0) and (i%5==0):
		l.append(str(i))
print (','.join(l))


'''
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
'''


