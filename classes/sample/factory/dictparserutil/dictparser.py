class Dictparser:

	def __init__(self,**kwargs):
		pass

	def __getbyval(self, data, val):
		if not type(data) == dict:
			return None, None
		for k, v in data.items():
			if v == val:
				return k, v

			if type(v) == str:
				if type(val) == str:
					if v.lower() == val.lower():
						return k,v

			if type(v) == dict:
				found = self.__getbyval(v, val)
				if any(found):
					return found
		return None, None

	def __getbykey(self, data, key):
		if not type(data) == dict:
			return None, None

		for k, v in data.items():
			if k == key:
				return k, v

			if type(k) == str:
				if type(key) == str:
					if k.lower() == key.lower():
						return k,v

			if type(v) == dict:
				found = self.__getbykey(v, key)
				if any(found):
					return found
		return None, None

	def __getbypath(self,data,path):
		if not type(data)==dict:
			return None,None
		subdict = data
		try:
			for k in path[:-1]:
				subdict = subdict[k]
		except KeyError:
			return None,None
		return path[-1], subdict[path[-1]]

	def findindict(self, data, key=None, val=None,path=None):
		assert key or val or path
		if key:
			k, v = self.__getbykey(data=data, key=key)
		elif val:
			k, v = self.__getbyval(data=data, val=val)
		else:
			k,v = self.__getbypath(data=data, path=path)
		if v:
			if not path:
				path = self.__createpath(data=data, val=v)
				path.append(k)
		return path, k, v

	def setval(self, data, path, val):
		subdict = data
		for k in path[:-1]:
			subdict = subdict[k]
		subdict [path[-1]] = val

	def __createpath(self, data, val, path=None):
		if not path:
			path = []
		if not type(data) == dict:
			return path

		for key, value in data.items():
			found = self.__getbyval(value, val=val)
			if any(found):
				path.append(key)
				self.__createpath(value, val=val,path=path)

		return path