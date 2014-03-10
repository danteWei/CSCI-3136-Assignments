from Stack import *

li=stack();

for i in range(0, 9):
	li.push(i);
print li;

node=li.peak();
print node;
print li;

node=li.pop();
print node;
print li;

print li.count();

li.clear();
print li.count();
print li;
