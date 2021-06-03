class MyException(TypeError):
  pass 


def ff():
  raise MyException("ppp")

try:
  ff()
except TypeError as e:
  print("mine", e)
except MyException:
  print("some other")