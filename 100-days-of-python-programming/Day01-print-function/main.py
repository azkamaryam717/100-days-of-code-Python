print("Hello world")
print(6)
print(5.6)
print(False)

#we can print multiple data types at once

print("Pakistan",5,True)

# By default python interpreter will see comma as a separation and will not print comma 
# But will separate the objects with a space unless you use sep

print("Pakistan","China","Bangladesh")

#sep means a separator we can use any string to separate the objects in print statement. 
# By default it's " "(space)

print("Pakistan","China","Bangladesh",sep="/")
print("Pakistan","China","Bangladesh",sep="-")

# end also uses string to end that print statement what happens after that statement ends.
print("Pakistan","China","Bangladesh")
print("Korea")

# By default it's \n (new line) but we can choose any string to attach that print statement to the next one

print("Pakistan","China","Bangladesh",end=" and ")
print("Korea")

# we xan use both sep and end collectively

print("Pakistan","China","Bangladesh",sep=",", end=" and ")
print("Korea")
