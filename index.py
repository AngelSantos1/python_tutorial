l = [8,3,2,7,6,7]
b = 0
a = 7

while b < len(l):
    c = l[b]
    if a == c:
        print(b)
        break
    b = b + 1

