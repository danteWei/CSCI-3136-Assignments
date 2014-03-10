#!/usr/bin/python

from LinkedList import *
import sys, string, tokenize

tokens = iter( sys.stdin.read().split() )
cur_token = None
output = ""
error = False
li=LinkedList();

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
  print "S -> Atoms" 
  parseAtoms(newList);
  li=newList;
  

def parseAtoms(listTmp):
  tok = lookahead()
  if tok == None or tok == ")":
    print "Atoms -> epsilon" 
  else:
    print "Atoms -> Atom Atoms" 
    parseAtom(listTmp)
    parseAtoms(listTmp);

def parseAtom(listTmp):
  tok = lookahead()
  if tok == "(":
    newList=LinkedList();
    print "Atom -> List"
    listTmp.prepend(newList);
    parseList(newList);
  elif tok == "'":             # quote
    print "Atom -> ' Atom" 
    next_token()
    parseAtom(listTmp);
  elif( str(tok).isdigit() ):       # integer
    print "Atom -> int" 
    listTmp.prepend(str(tok));
    next_token()
  else:                        # identifier
    print "Atom -> id" 
    listTmp.prepend(str(tok));
    next_token()

def parseList(listTmp):
  global error
  tok = lookahead()
    
  print "List -> Atoms" 
  next_token()
  parseAtoms(listTmp);
  tok = next_token()
  if tok != ")":
    error = True


parseS()
tail = lookahead()
if error or tail != None:
  print "Syntax Error"
else:
  print "Valid Program"

print li;
