
# list
f = list()
f.append("hello")
print(f[0] == "hello")
f.append("world")
print(f)
del f[1]
print(f)

# list comprehension

f = [i for i in range(40) if i % 2 == 0]

# double loop
double = [x*y for x in range(1,10) for y in range(1,2)]


# tuples are like lists but are immutable (you cant even change the values of indexes)
f = (1,2,3,4,5)
i, j, *k = f
#i=1,j=2, k=(3,4,5)

def func():
  return (1,2)
p, o = func()
#p=1, o=2

# sets
f = set()
f.add(1)
f.add(2)
f.add(3)
f.add(1) # does nothing, all values are unique

s = {1, 5, 8, 9}

s.union(f) # 1, 2, 3, 5, 8, 9
s.intersection(f) # 1
s.difference(f) # 5,8,9
f.difference(s) # 2, 3

# you cant index a set, but you can iterate over it using `for i in f`


# dictionaries
f = dict()
f["hello"] = "world"
f["lala"] = "land"
f["motion"] = "stagnation"

f.keys() #iterable which returns [hello, lala, motion]; you can use the in operator
f.values() #iterable which returns [world, land, stagnation]; you can use the in operator

try:
  f["sdlsdkjfsdf"]
except:
  print("dont do that")

f.get("sdfsdfsdfsdf") # returns none



