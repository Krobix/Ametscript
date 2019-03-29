import sys
import threading

lastId = 0 #Ids used for object pointers

class aObject:
	def __init__(self, name, value, type):
		global lastId
		self.name = name
		self.value = value
		self.aType = type
		self.id = lastId + 1
		self.attributes = {}
		lastId += 1
		
		
class aString(aObject):
	def __init__(self, name, value):
		super().__init__(name, value, "string")
		self.name = name
		self.value = str(value)
		self.aType = "string"
		
class aNum(aObject):
	def __init__(self, name, value):
		super().__init__(name, value, "number")
		self.name = name
		self.value = value

		
		
class aBool(aObject):
	false = aNum("false", 0)
	true = aNum("true", 1)
	
	def __init__(self, name, value):
		super().__init__(name, value, "bool")
		self.name = name
		self.value = value
		 
	
class aArray(aObject):
	def __init__(self, name):
		super().__init__(name, [], "array")
		self.name = name
		self.value = []
		self.aType = "array"
		
class aError(aObject):
	def __init__(self, name):
		super().__init__(name, name, "error_obj")
		self.name = name
		self.aType = "error"
	def aRaise(self, text, ln):
		print("EXCEPTION: " + self.name + ": " + text + " on line " + str(ln) + "\n")
		input("Press enter to exit...\n")
		sys.exit()
		
		
class aStream(aObject):
	def act(self, val):
		pass
	def getVal(self):
		return self.id
	def delVal(self):
		pass
	def setVal(self, val):
		self.act(val)
	def __init__(self, name, act):
		super().__init__(name, 0, "stream")
		self.act = act
		self.attributes["act"] = self.act
		
	value = property(getVal, setVal, delVal, )
		
		
	
	
TypeErr = aError("TypeError")
		
		
def convertObject(obj, newType, ln, attr=None): 
		try:
			if newType == "string":
				return aString(obj.name, str(obj.value))
			elif newType == "num":
				return aNum(obj.name, int(obj.value))
			elif newType == "stream":
				return aStream(obj.name, attr["act"])
		except TypeError:
			TypeErr.aRaise("Invalid Value For Type " + obj.type, ln)
			
		
		
