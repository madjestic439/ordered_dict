###!src/bin/python

"""code testing file"""

from sortable_dict import *

test1 = SortableDict()
print(test1)

d = {'a':1, 'b':2, 'c':3}
test2 = SortableDict(d)
print(test2)

test3 = SortableDict(z=26, y=25, x=24, w=23)
print(test3)
