x = '123'
y = '1'
z = x.ljust(30)+y
k = x.ljust(30)

print(z)
print(len(k))
print('{0:<10}'.format(x))
print('{0:05d}'.format(int(x)))
print('{0:07.2f}'.format(123.34))
print('{0:0<10}'.format(123))
print('{0:x>10d}'.format(123))
print('{0:x>8.2f}'.format(123.52))