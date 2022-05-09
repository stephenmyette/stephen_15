animals = ["bird", "fox", "cat", "rat", "alligator"]


print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
print(animals[4])

print(animals[-1])

print(animals[2:])

animals.append("giraffe")

moreAnimals = ["monkey", "ant eater", "red panda"]

animals.extend(moreAnimals)

animals.insert(4, "snake")

animals.pop(3)

animals.remove("snake")

del animals[2]

#deletes entire list
# del animals 

for counter in animals:
    print(counter)
    
