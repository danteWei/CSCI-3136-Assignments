#!/local/bin/python

import sys, string, tokenize

tokens = iter( sys.stdin.read().split() )
cur_token = None
procs = ['let', 'define']

class ParseError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class EvalError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

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


def add( a, b ):
  return a + b

def sub( a, b ):
  return a - b

def mul( a, b ):
  return a * b

def div( a, b ):
  return a / b


def do_arith_op( op, l ):
  if len( l ) < 1:
    raise EvalError( op )

  r = do_eval( l[0] )
  if not isinstance( r, int ):
    raise EvalError( op )

  r = l[0]
  for o in l[1:]:
    i = do_eval( o )
    if isinstance( i, int ):
      r = op( r, i )
    else:
      raise EvalError( op )
 
  return r


def do_eval( a ):
  if isinstance( a, list ): # list  
    if len( a ) < 1:
      raise EvalError( '( )' )

    op = do_eval( a[0] )

    f = a
    a = None

    if op == "+":
      a = do_arith_op( add, f[1:] )
    elif op == "-":
      a = do_arith_op( sub, f[1:] )
    elif op == "*":
      a = do_arith_op( mul, f[1:] )
    elif op == "/":
      a = do_arith_op( div, f[1:] )
    elif op == "'":
      if len( f ) > 1:
        a = f[1]
    elif op == "car":
      if len( f ) > 1:
        l = do_eval( f[1] )
        if isinstance( l, list ) and len( l ) > 0:
          a = l[0]
    elif op == "cdr":
      if len( f ) > 1:
        l = do_eval( f[1] )
        if isinstance( l, list ) and len( l ) > 0:
          a = l[1:]
    elif op == "cons":
      if len( f ) > 2:
        h = do_eval( f[1] )
        t = do_eval( f[2] )
        if isinstance( t, list ):
          a = [ h ] + t
    elif op == "list":
      a = []
      for b in f[1:]:
        a = a + [do_eval( b )]
    elif op in procs:
      a = f
    else:
      raise EvalError( 'unknown proc: ' + str( op )  ) 

    if a == None:
      raise EvalError( op )

    return a
  elif str(a).isdigit():   # int
    return a
  else:                    # id
    return a


def parseS():
  return parseAtoms()
  

def parseAtoms():
  tok = lookahead()
    
  if tok == None or tok == ")":
    return []
  else:
    return parseAtom() + parseAtoms()
   

def parseAtom():
  tok = lookahead()
    
  if tok == "(":
    l = [ parseList() ]
  elif tok == "'":             # quote
    next_token()
    l = [[tok] + parseAtom()]
  elif( str(tok).isdigit() ):  # integer
    next_token()
    l = [int( tok )]
  elif tok != None:         # identifier
    next_token()
    l = [tok]
  else:
    raise ParseError( 'Atom' )

  return l


def parseList():
  tok = next_token()

  if tok == '(': 
    l = parseListBody()
    tok = next_token()
    if tok != ")":
      raise ParseError( 'List' )
  else:
    raise ParseError( 'List' )

  return l


def parseListBody():
  tok = lookahead()
  l = []

  if tok in procs: 
    l = parseProc()

  return l + parseAtoms()


def parseProc():
  tok = next_token()

  if not tok in procs: 
    raise ParseError( 'Proc' )

  return [tok]


def print_result( l ):
  if isinstance( l, list ):
    print "(",
    for a in l:
      print_result( a )
    print ")",
  else:
    print l,
 
def eval_result( l ):
  for a in l:
    print_result( do_eval( a ) )
 
try:
  l = parseS()
  if lookahead() != None:
    raise ParseError( 'S' )
  eval_result( l )
  print ""
except ParseError as p:
  print "Syntax Error while parsing " + str( p ) + " production"
except EvalError as p:
  print "Evaluation Error while evaluating " + str( p )


