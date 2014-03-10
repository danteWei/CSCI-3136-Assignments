# Author: Xinjing Wei


class Node(object):
	def __init__(self, data=None, nextNode=None):
		self.data=data;
		self.nextNode=nextNode;
	
	def __repr__(self):
		if self.data != None:
			return str(self.data);
		else:
			return '';


class LinkedList(object):
	# Constructor
	def __init__(self):
		self.head=None;
		self.size=0;
	
	# Add a node to the end of the list
	def append(self, data):
		n=Node();
		n.data=data;
		if self.size == 0:
			self.head=n;
		elif self.size == 1:
			self.head.nextNode=n;
		else:
			tmp=self.head;
			while tmp.nextNode != None:
				tmp=tmp.nextNode;
			tmp.nextNode=n;
		
		self.size=self.size+1;
	
	# Add a node to the front of the list
	def prepend(self, data):
		n=Node();
		n.data=data;
		if self.size == 0:
			self.head=n;
		else:
			n.nextNode=self.head;
		
		self.size=self.size+1;
		self.head=n;
	
	# Returns the size of the list
	def length(self):
		return self.size;

	# Clear a list
	def clear(self):
		self.size=0;
		self.head=None;

	# Delete the first node
	def removeFirst(self):
		tmp=self.head;
		if self.size == 0:
			print 'The list is empty!';
		elif self.size == 1:
			self.clear();
		else:
			self.head=self.head.nextNode;
			self.size-=1;
		return tmp;

	# Remove the last node
	def removeLast(self):
		tmp=None;
		if self.size == 0:
			print 'The list is empty!';
		elif self.size == 1:
			tmp=self.head;
			self.clear();
		else:
			curr=self.head;
			while curr.nextNode.nextNode != None:
				curr=curr.nextNode;
			tmp=curr.nextNode;
			curr.nextNode=None;
			self.size=self.size-1;
		return tmp;

	# Remove a node
	def remove(self, index):
		tmp=None;
		if index >= self.size or index < 0:
			print 'Can\'t remove! Index out of bound!';
		elif self.size == 0:
			print 'The list is empty!';
		elif self.size == 1:
			tmp=self.head;
			self.clear();
		elif self.size-1 == index:
			tmp=self.removeLast();
		else:
			i=0;
			curr=self.head;
			while i < index-1:
				curr=curr.nextNode;
				i=i+1;
			tmp=curr.nextNode;
			curr.nextNode=curr.nextNode.nextNode;
			self.size=self.size-1;
		return tmp;
	
	# return true if the list is empty
	def isEmpty(self):
		return (self.size == 0);

	# Returns the string representation of the list
	def __repr__(self):
		strs='(';
		if self.size == 0:
			print 'The list is empty!';
		else:
			tmp=self.head;
			while tmp.nextNode != None:
				strs+=str(tmp.data)+' ';
				tmp=tmp.nextNode;
			strs+=str(tmp.data);
		strs+=')';
		return strs;

	
