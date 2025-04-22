# #delete a folder recursively:
# # from pathlib import Path

# def rmdir(directory):
#     directory = Path(directory)
#     for item in directory.iterdir():
#         if item.is_dir():
#             rmdir(item)
#         else:
#             item.unlink()
#     directory.rmdir()

# printing a nested dictionary items:
# nested dictionaries:
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

# def printdict(subdict):
#     for key,val in subdict.items():
#         print(f"key: {key}, val: {val}")
#         if isinstance(val,dict):
#             printdict(subdict=val)

# printdict(subdict=nesteddict)

#check if a key exists in a nested dict:
def keyexists(subdict,keytofind):
    found = False
    for key,val in subdict.items():
        if key == keytofind:
            found = True
            break
        if isinstance(val,dict):
            found = keyexists(subdict=val,keytofind=keytofind)
    return found

found = keyexists(subdict=nesteddict,keytofind="hunters")
print(found)
found = keyexists(subdict=nesteddict,keytofind="aquatic")
print(found)


def findbykey(keytofind, dictoparse, address=""):
    key, val = None, None
    for k, v in list(dictoparse.items()):
        indextosnip = len(address)
        address = address + "..." + k
        if k == keytofind:
            key, val = k, v
        elif isinstance(v, dict):
            key, val, address = findbykey(keytofind, v, address)
        if key:
            address = address.strip('.')
            break
        else:
            address = address[:indextosnip]
    return key, val, address

def findbykey(keytofind, dicttoparse):
    key,val,address = findbykey(keytofind=keytofind,dictoparse=dicttoparse)
    if key:
        address = tuple(address.split("..."))
    return key, val, address