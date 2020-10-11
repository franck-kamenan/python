print("\n")

#BOOLEANS

print(10 > 9)
print(10 == 9)
print(10 < 9)
print("\n")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is NOT greater than a")

print("\n")
#bool() method
print(bool("Hello"))
print(bool(15))
print(bool(True))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(0))
print(bool(None))
print(bool(False))

print("\n")
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")   

print("\n")
#isinstance() method
print(isinstance(a, int))     

print("\n")