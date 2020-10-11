print("\n")
x = "awesome" #global
def myfunc():
    x = "fantastic" #local
    print("I am " + x)

myfunc()

print("I am " + x)
print("\n")