#pickle files are used to hold python objects
# Unlike json, it is python specific and cannot be used on any other platform

import pickle
import pathlib

mydict = {
	"name":"Alan",
	"wife":"Judy",
	"children":("Mary","John")
}
#use write bytes or read bytes mode to operate on such files

filepath = pathlib.Path("SimthsFamily.pkl")
# pickle.dump(mydict,filepath.open('wb'),pickle.HIGHEST_PROTOCOL)
# data = pickle.load(filepath.open("rb"))
# print(data)


