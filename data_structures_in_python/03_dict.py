#ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#ref: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

#Dictionaries are data structures that store named variables(key) and values

# from testnesteddict import books
# emptydict = {}

simpledict = {"one":1,"two":2,"nested":{"mylist":[2,3,4,56]}}
# print(simpledict)
# anotherdict = dict(dc="superman",marvel="thor")
# print(anotherdict)

# #Accessing value of key from a dictionary:
# print(simpledict["one"])
# # doesnotexist = simpledict["Three"]

# print(simpledict.get("one"))
# doesnotexist = simpledict.get("Three")
# print(doesnotexist)

# #Adding key,val to dictionary:
# simpledict["Three"] = 3
# print(simpledict)

# #removing key from dict:
# val = simpledict.pop("Three")
# print(val)
# print(simpledict)

# #Changing value of a key:
# simpledict["one"] = 1.00
# print(simpledict)
# simpledict.update(one=1,two=2.00)
# print(simpledict)

#get all keys:
# firstlevelkeys = simpledict.keys()
# print(firstlevelkeys)

# #Check if key exists:
# key = "Three"
# if key in simpledict:
#   print("Exists")
# else:
#   print("doesnot exist")

# #Return a new view of the dictionary’s items
# dictitemsastuple = simpledict.items()
# print(dictitemsastuple)
# print(dict(dictitemsastuple))

# #iterating over a dictionary:
# for key,val in simpledict.items():
#   print(f"key: {key}, value: {val}")

#nested dictionaries:
nesteddict = {
    "animals":{
        "mammals":{
            "carnivorous":"Tiger",
            "noncarni":"Cow",
            "omnivorous":"Human"
        }
    },
    "birds":{
        "hunters":"Eagle",
        "scavengers":["Crows","Vulture"],
        "pets":["parrot","cockatoo"]
    }    
}

print(nesteddict)
# print(nesteddict["birds"])
# print(nesteddict["birds"]["scavengers"])
# print(nesteddict["birds"]["scavengers"][0])