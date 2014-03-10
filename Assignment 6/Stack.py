# Author: Xinjing Wei

from LinkedList import *

class Stack(object):
	# Constructor
	def __init__(self, li=LinkedList(), size=0):
		self.li=li;
		self.size=size;

	# Push a node into the stack
	def push(self, data):
		n=Node();
		n.data=data;

		self.li.prepend(n);
		self.size+=1;

	# Pop a node
	def pop(self):
		node=None;
		if self.li.isEmpty():
			print 'Can\'t pop, the stack is empty!';
		else:
			node=self.li.removeFirst();
			self.size-=1;
		return node;

	# Return the top node without deleting it
	def peak(self):
		node=self.li.head;
		if self.size == 0:
			print 'The stack is empty!';
		return node;

	# Return how many items in the stack
	def count(self):
		return self.size;

	# Clear the stack
	def clear(self):
		self.li.clear();
		self.size=0;
	
	# Return true if the stack is empty
	def isEmpty(self):
		return self.li.isEmpty();

	# print stack
	def __repr__(self):
		return self.li.__repr__();
