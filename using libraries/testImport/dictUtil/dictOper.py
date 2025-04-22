import sys
print(sys.path)

from ..listUtil.listOper import sumMyList
from ..tupleUtil.tupleOper import sumMyTuple

def sumMyDict(obj):
	for key,val in obj.items():
		if isinstance(val,list):
			obj[key] = sumMyList(val)
		elif isinstance(val,tuple):
			obj[key] = sumMyTuple(val)
	return obj

if __name__ == "__main__":

	mydict = {
		"list1":[1, 2, 3, 4, 5],
		"tuple1":(1, 2, 3)
	}

	sumMyDict(mydict)
	print(mydict)