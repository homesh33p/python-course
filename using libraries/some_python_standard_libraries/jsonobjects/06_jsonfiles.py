#json is a data format, not a file type
#json objects can be saved in a json file

import json
import pathlib
mydict = {
	"name":"Alan",
	"wife":"Judy",
	"children":["Mary","John"]
}

# filepath = pathlib.Path("SimthsFamily.json")
# with filepath.open("w") as buffer:
# 	print(mydict)
# 	print(json.dumps(mydict,indent=4))
# 	json.dump(mydict,buffer,indent = 4)

# with filepath.open("r") as buffer:
# 	data = json.load(buffer)
# 	print(type(data))
# 	print(data)
# 	print(json.dumps(data,indent=4))
