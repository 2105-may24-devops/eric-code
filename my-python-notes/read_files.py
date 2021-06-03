
def read_basic():
  file = open("collections.py", "r")
  f = file.read()
  print(f)
  file.close()



def read_loop():
  myfile = open("collections.py", "r")
  while myfile:
      line  = myfile.readline()
      print(line)
      if line == "":
          break
  myfile.close()

if __name__ == "__main__":
  read_basic()
