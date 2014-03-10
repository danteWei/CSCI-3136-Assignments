#!/usr/bin/python

from LinkedList import *
from Stack import *
import sys, string, tokenize

tokens = iter( sys.stdin.read().split() )
cur_token = None
output = ""
error = False
li=LinkedList();
st=Stack();

def lookahead():
  global cur_token

  if cur_token == None:
    try:
      cur_token = tokens.next()
    except:
      cur_token = None

  return cur_token


def next_token():
  global cur_token

  n = lookahead()
  cur_token = None
  return n


def parseS():
  global li;
  newList=LinkedList();
  newStack=Stack();
  print "S -> Atoms" 
  parseAtoms(newList, newStack);
  li=newList;
  

def parseAtoms(listTmp, stack):
  tok = lookahead()
  if tok == None or tok == ")":
    print "Atoms -> epsilon" 
  else:
    print "Atoms -> Atom Atoms" 
    parseAtom(listTmp, stack)
    parseAtoms(listTmp, stack);

def parseAtom(listTmp, stack):
  tok = lookahead()
  if tok == "(":
    newList=LinkedList();
    print "Atom -> List"
    listTmp.prepend(newList);
    parseList(newList, stack);
  elif tok == "'":             # quote
    print "Atom -> ' Atom" 
    next_token()
    parseAtom(listTmp, stack);
  elif( str(tok).isdigit() ):       # integer
    print "Atom -> int" 
    stack.push(str(tok))
    listTmp.prepend(str(tok));
    next_token()
  else:                        # identifier
    print "Atom -> id" 
    listTmp.prepend(str(tok));
    next_token()

def parseList(listTmp, stack):
  global error
  tok = lookahead()
    
  print "List -> Atoms" 
  next_token()
  parseAtoms(listTmp, stack);
  tok = next_token()
  if tok != ")":
    error = True

def eval(stack, operator):
	valid=True;
	if operator == '+':
		result=0;
		while (not stack.isEmpty()) and valid:
			try:
				result+=int(stack.pop);
			except:
				valid=False;
				break;
		return result;
	if operator == '*':
		result=1;
		while (not stack.isEmpty()) and valid:
			try:
				result*=int(stack.pop);
			except:
				valid=False;
				break;
		return result;

	if operator == '-':
		result=stack.pop();
		while(not stack.isEmpty()) and valid:
			try:
				result-=stack.pop();
			except:
				valid=False;
				break;
		return result;

	if operator == '/':
		result=stack.pop();
		while(not stack.isEmpty()) and valid:
			try:
				result/=stack.pop();
			except:
				valid=False;
				break;
		return result;

	if valid == False:
		print 'Evaluation Error';

parseS()
tail = lookahead()
if error or tail != None:
  print "Syntax Error"
else:
  print "Valid Program"

print li;
