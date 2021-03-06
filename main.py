###!src/bin/python

"""code testing file"""

from sortable_dict import *

test1 = SortableDict()
print(test1)

d = {'a':1, 'b':2, 'c':3}
test2 = SortableDict(d)
print(test2)

test3 = SortableDict(z=26, y=25, x=24, w=23, a=1, b=2, c=3)
print(test3)

print(test3['x'])
test3['x'] = 100
print(test3)
test3['x'] = 24
print(test3)
print("'w' is in: {}".format('w' in test3))
del test3['w']
print("'w' is in: {}".format('w' in test3))
print("lenght: {}".format(len(test3)))
print(test3)
test3['w'] = 23
print(test3)
print("'w' is in: {}".format('w' in test3))
print("lenght: {}".format(len(test3)))
print("sorted: {}".format(test3.sort()))
print("reverse: {}".format(test3.reverse()))

for k in test3 :
	print(k)

for ke in test3.keys():
	print("key: {}".format(ke))

for ve in test3.values():
	print("value: {}".format(ve))

for ki, vi in test3.items():
	print("{}: {}".format(ki, vi))

print(test1 + test2)

print(test2 + test3)

test2['j'] = 10
test3 += test2
print(test3)

print(test3.values())
print(test3.keys())
