# for project 0, keep in mind that there's a pip package called blessings -- for creating text
# based interfaces



# python follows an LEGB namespace pattern
# this might be in the qc test
# namespaces: a context in which variables live
# when a variable is called, 
# first the local namespace is called
# then any enclosing namespace
# then, the global namespace
# then the built-in namespace (print, str)

var = 5 # global
if True:
  y = 10 # global, python doesnt have block scope

# in python, functions and classes have their own namespace
def func():
  v = 6 # local
  # however
  global var 
  var = 5 # now this is global


def func(x):
  r = x # enclosing for func3()
  def func1():
    return r == 3
  return func1

# important things to know for qc/quiz
# 