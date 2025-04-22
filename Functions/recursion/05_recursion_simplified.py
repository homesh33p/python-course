#recursion via reduction

#To sum numbers in a list:

# def sum(arr,mysum):
# 	mysum = mysum + arr[0]
# 	mysum = mysum + arr[1]
# 	mysum = mysum + arr[2]
# 	return mysum

# def sum(arr,mysum):
# 	mysum = mysum + arr[0]
# 	arr = arr[1:]
# 	mysum = mysum + arr[0]
# 	arr = arr[1:]
# 	mysum = mysum + arr[0]
# 	return mysum

def sum(arr,mysum):
	mysum = mysum + arr[0]
	if len(arr) > 1:
		arr = arr[1:]
		mysum = mysum + arr[0]
	if len(arr) > 1:
		arr = arr[1:]
		mysum = mysum + arr[0]
	if len(arr) > 1:
		arr = arr[1:]
		mysum = mysum + arr[0]
	return mysum

def sum(arr,mysum):
	mysum = mysum + arr[0]
	if len(arr) > 1:
		arr = arr[1:]
		mysum = mysum + arr[0]
		if len(arr) > 1:
			arr = arr[1:]
			mysum = mysum + arr[0]
			if len(arr) > 1:
				arr = arr[1:]
				mysum = mysum + arr[0]
			else:
				return mysum
		else:
			return mysum
	else:
		return mysum

def sum(arr,mysum=0):
	mysum = mysum + arr[0]
	if len(arr) > 1:
		arr = arr[1:]
		mysum = mysum + arr[0]
		if len(arr) > 1:
			arr = arr[1:]
			mysum = mysum + arr[0]
			if len(arr) > 1:
				arr = arr[1:]
				mysum = mysum + arr[0]
	return mysum

def sum(arr,mysum=0):
	mysum = mysum + arr[0]
	if len(arr)>1:
		arr = arr[1:]
		mysum = sum1(arr, mysum)
	return mysum

print(sum([1,2,3],0))

