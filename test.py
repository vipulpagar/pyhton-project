a=(1,2,3,4,8)
b=list(a)
b[4]=5
print(b)
b.extend([6,7,8,9,10])
print(b)
a=tuple(b)
print(a)
