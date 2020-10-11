print("\n")
x = "awesome" #global
def myfunc():
    global x
    x = "fantastic" #local
    print("I am " + x)

myfunc()

print("I am " + x)
print("\n")