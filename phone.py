#A python program that stores and sorts the contact information of friends by using the concept of dictionary.

dict1 = {}

n = int(input("Enter the number of friends: "))

for i in range(n):
        name = input("Enter the names of friends: ")
        phonenumber = int(input("Enter phone number: "))
        dict1[name] = phonenumber 
                
for i in dict1:
        print(i,':',dict1[i])
    
a = input("Enter the new entry's name: ")
b = input("Enter the new entry's phone number: ")
dict1[a] = b

print("The updated dictionary is: ")
for i in dict1:
        print(i,':',dict1[i])
    
x = input("Enter the friend's name whose number is to be modified: ")

if x in dict1:
        y = input("Enter the new number: ")
        dict1[x] = y

z = input("Enter a name to be checked: ")

if z in dict1:
        print("Exists")
else:
        print("Does not exist")

print("The sorted dictionary is: ")

for i in sorted(dict1):
        print(i,':',dict1[i])
