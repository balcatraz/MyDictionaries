from ast import Delete
from os import remove
from webbrowser import get


phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

print()
print("*****  start section 1 - print dictionary ********")
print()


print(phonebook)
print(type(phonebook))

phone = phonebook["Chris"]

print(phone)

print(len(phonebook))

mydictionary = dict(m=8, n=9)

print(mydictionary)


print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()


name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(name, "is not in the phonebook")


print()
print("*****  end section 2 ********")
print()


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print([phonebook])
phonebook["chris"] = "555-0123"

phonebook["Chris"] = "555-4444"
print([phonebook])

print()
print("*****  end section 3 ********")
print()


print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()


del phonebook["chris"]

print(phonebook)


print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys ********")
print()

for key in phonebook:
    print(key)
    print(phonebook[key])

print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()

for val in phonebook.values():
    print(val)


print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - iterate through both key and value pair********")
print()


for phonebook_tuple in phonebook.items():
    print(phonebook_tuple)


for key, val in phonebook.items():
    print(key)
    print(val)

print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using get and clear  ********")
print()

phone = phonebook.get("Chris", "Not found")
print(phone)

newPhonebook = phonebook
print(newPhonebook)
###newPhonebook.clear()
print(newPhonebook)

print()
print("*****  end section 8 ********")
print()


print()
print("*****  start section 9 - using pop method ********")
print()

remove = phonebook.pop("Joanne", "not found")
print(remove)
print(phonebook)

print()
print("*****  end section 9 ********")
print()


print()
print("*****  start section 10 - using popitem ********")
print()

a = phonebook.popitem()
print(a)
print(phonebook)

print()
print("*****  end section 10 ********")
print()


phonebook["Joanne"] = "555-2222"
phonebook["Heidy"] = "555-3333"

print()
print("*****  start section 11 - using random and converting to list ********")
print()

import random

listOfKeys = list(phonebook)
randKey = random.choice(listOfKeys)
print(randKey)
print(phonebook[randKey])

print(phonebook[random.choice(list(phonebook))])

print()
print("*****  end section 11 ********")
print()
