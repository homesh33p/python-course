import sys

from listUtil.listOper import sumMyList
from tupleUtil.tupleOper import sumMyTuple
from dictUtil.dictOper import sumMyDict

def sumMyIterator(obj):
	if isinstance(obj,list):
		return sumMyList(obj)
	elif isinstance(obj,tuple):
		return sumMyTuple(obj)
	elif isinstance(obj,dict):
		return sumMyDict(obj)

if __name__=="__main__":
	# print(f"name as Script: {__name__}")
	print(sys.path[0])
	mysum = sumMyIterator([-2,-1,0,1,2])
	print(mysum)
	mydict = {
		"list1":[1, 2, 3, 4, 5],
		"tuple1":(1, 2, 3)
	}

	mysum = sumMyIterator(mydict)
	print(mysum)