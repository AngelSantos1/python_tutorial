#Sorting
#Design a function "bubble_sort(x)" that sorts x using the bubble sort algorithm. (Don't use sorted() or x.sort())
#For example, sort([2, 7, 3, 6]) returns [2, 3, 6, 7] and sort([8, 4, 2, 6]) returns [2, 4, 6, 8]


#def osomething()

i = 0
l = [5,8,3,2,7,2,6,9]

while i < len(l):
	
	j = 0
	while j < len(l) - i - 1:
   
		if l[j+1] < l[j]:
			fred = l[j+1] 
			l[j+1] = l[j] 
			l[j] = fred
		j = j + 1
 	
	i = i + 1

print(l)

