entry = int(input("enter a number: "))
if entry % 2 == 0:
  print("Your number is even.")
elif entry % 2 == 1:
  print("Your number is odd")
else:
  print("what could your number possibly be?")


entry = int(input("enter another number:"))
if entry > 0:
  print("your number is positive")
elif entry < 0:
  print("your number is negative")
else:
  print("your number is zero")

