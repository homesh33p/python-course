import sys
from .tupleChecker import checkTuple

def sumMyTuple(obj):
	obj = checkTuple(obj)
	return sum(list(obj))

# print(__name__)

if __name__ == "__main__":
	# print(f"name As script: {__name__}")
	# print(sys.path[0])
	mysum = sumMyTuple((1,2,"abc"))
	print(mysum)