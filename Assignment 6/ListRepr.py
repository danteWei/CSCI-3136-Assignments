# Author: Xinjing Wei
# Author of the original Parser class: Alex BrodSky; Edited by Xinjing Wei



from LinkedList import *
from Stack import *
import sys, string, tokenize


class Parser(object):
	def __init__(self):
		self.tokenS = iter( sys.stdin.read().split() )
		for i in self.tokenS:
			print i
		self.curToken = None;
		self.output = ""
		self.error = False
	
	def lookahead(self):
		if self.curToken == None:
			try:
				self.curToken = self.tokenS.next()
			except:
				self.curToken = None
		return self.curToken
	

	def next_token(self):

		n = self.lookahead()
		self.curToken = None
		return n


	  

	def parseAtoms(self):
		tok = self.lookahead()
    
		if tok == None or tok == ")":
			print "Atoms -> epsilon" 
		else:
			print "Atoms -> Atom Atoms" 
			self.parseAtom()
			self.parseAtoms()


	def parseAtom(self):
		tok = self.lookahead()
    
		if tok == "(":
			print "Atom -> List"
			self.parseList()
		elif tok == "'":             # quote
			print "Atom -> ' Atom" 
			self.next_token()
			self.parseAtom()
		elif( str(tok).isdigit() ):       # integer
			print "Atom -> int" 
			self.next_token()
		else:                        # identifier
			print "Atom -> id" 
			self.next_token()
    
	def parseList(self):


		tok = self.lookahead()
    		print "List -> Atoms" 
		self.next_token()
		self.parseAtoms()
		tok = self.next_token()
		if tok != ")":
			self.error = True
	
	def parseS(self):
		print "S -> Atoms" 
		self.parseAtoms();

	def startParse(self):
		self.parseS()
		tail = self.lookahead()
		if self.error or tail != None:
			print "Syntax Error"
		else:
			print "Valid Program"
		return self.error, self.tokenS;


class ListRepr(object):
	# Attributes
	token=None;
	errorFlag=False;

	# Constructor
	def __init__(self):
		p=Parser();
		error, tokens=p.startParse();
		self.errorFlag=error;
		self.token=tokens;
		if self.errorFlag != False:
			sys.exit(1);

	# Determine if a character is an atom but not a list
	def isAtom(char):
		if char == '+' or char == '-' or char == '*' or char == '/':
			return True;
		elif str(char).isdigit():
			return True;
		return False;


	def parseList(self, index, s):
		li=LinkedList();
		i=0;
		for i in range (index, len(s)):
			# If it is a list
			if s[i] =='(' or s[i] == '\'':
				if i != index:
					index, tmp=self.parseList(i+1, s);
					li.prepend(tmp);
				else:
					continue;
			elif s[i] == ')':
				break;
			else:
				li.prepend(s[i]);
		return i, li;

	def hasParenthesis(s):
		flag=False;
		for char in s:
			if char == '(':
				flag=True;
				break;
		return flag;

	def parseIn(self):
		tokens=self.token;
		listRepr=LinkedList();
		tok={};
		lists='';
		j=0;
		for i in tokens:
			j, tok[i]=self.parseList(i);
		for i in tok:
			print tok[i];


listR=ListRepr();
n, l=listR.parseList(0, '(+1(*23)(*24))');
print l;
