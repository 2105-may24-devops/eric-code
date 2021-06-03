# common methods, you can find them in the docs

# is___() empty/lower/upper
# lower, upper, capitalize
# replace(replaced_substring, replacing_substring)
# split splits string on given pattern, returns list
# strip drops leading and trailing chars


# on slices: f[0:5] 0 is included, 5 is excluded--hence the slice is f[0] to f[4]; if you want the entire array f[0:len(f)]
# f[0:len(f):2] grabs every other element in slice, you can also go f[::2]
import math

print("hello, {1}, welcome to {0}. The weather is really nice at {2:.1f} fahrenheit".format("arek", "moscow", 78.916789))


verb = "running"
noun = "lalaland"
print(f"Herbert is {verb} to {noun.capitalize()}")


print()
print("float rounding %.4f. this is %s with %s decimals" % (math.pi, "pi", 4))

alphabet = "abcdefghijklmnopqrstuvwxyz"

import time
i : int = 0
while True:
  time.sleep(1)
  print(alphabet[i % len(alphabet)])
  i+=1


class test_doc:
  def pop_lock(self):
    ''' 
      this returns 10
    '''
    return 10