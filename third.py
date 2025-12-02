# vegetable = {
#    "potato" : 100,
#    "tomato": 10,
#    "spinach": 50,
#     "total" : [50, 60, 90]
# }

# print(vegetable["total"])

# gi = {}
# print(type(gi))

# go = set()
# print(type(go))

# print(vegetable.items()) # this function is used to list all the items in the dictionary

# print(vegetable.keys()) # this will print the keys 

# print(vegetable.values()) # this will provide all the values 

# vegetable.update({"tomato": 50, "capsicum": 80})
# print(vegetable.items())

# # print(vegetable["onion"])
# print(vegetable.get("onion")) 



# s = {1,2,3,4,"harry", True}
# print(s)
# print(type(s))

# s.add("mobile")
# s.add(8080) # this will not be added in the set
# s.add(553)

# print(s)

# s.remove("mobile")
# print(s)

# r ={1,2,34,"fwew", 'gafwef'}
# print(s.union(r))

# print(s.intersection(r))


# di = {"utkarsh": 90, "tushar": 84, "mayank": 78, "duggal": 90}
# key = input("please enter the name of student you want to change or add:")
# value =  int(input("please enter the makrs of student you want to change or add:"))

# di.update({key:value})
# print(di)

# di = {"utkarsh": 90, "tushar": 84, "mayank": 78, "duggal": 90}
# key = input("please enter the name of student you want to remove:")

# di.pop(key)
# print(di)


menu = {"drinks": ["tea", "coffee", "juice"], "snacks": ["samosa", "idli"]}

section = input("Which section you want to change (drinks/snacks): ")
ovalue = input("Which value do you want to change: ")
nvalue = input("What should be the new value: ")

i = menu[section].index(ovalue)
print(i)
menu[section][i] = nvalue
print(menu)
