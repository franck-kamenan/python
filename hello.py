print("\n")

#get character at position 1
x = "Bonjour, salut!"
print(x[1])

#negative indexing
print(x[-5])

#slicing
print(x[3:7])

#negative slicing
print(x[-4:-1])

#length
print(len(x))

#strip() method
print(x.strip())

#lower() method
print(x.lower())

#upper() method
print(x.upper())

#replace() method
print(x.replace("Bon", "Mal"))

#split() method
print(x.split(","))

#in
y = "onjo" in x
print(y)

#not in
y = "onjo" not in x
print(y)

#concatenation
z = "Bye!"
print(x + " " + z)

#format() method
age = 36
txt = "My name is John and I am {} years old."
print(txt.format(age))
numberOfCars = 2
numberOfSeats = 3
price = 400
myorder = "I want {} cars with {} seats at {} dollars."
print(myorder.format(numberOfCars, numberOfSeats, price))
#with index numbers
expensive = "{2} dollars is too much for {1} seats."
print(expensive.format(numberOfCars, numberOfSeats, price))

#escape character
print("We are the so-called \"Vikings\" from the north.")

print("\n")