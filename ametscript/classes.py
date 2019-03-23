import sys

class aObject:
	def __init__(self, name, value, type):
		self.name = name
		self.value = value
		self.aType = type
		self.attributes = {}
		
class aString(aObject):
	def __init__(self, name, value):
		self.name = name
		self.value = str(value)
		self.aType = "string"
		
class aInt(aObject):
	def __init__(self, name, value):
		self.name = name
		self.value = value
		
		
class aBool(aObject):
	false = aInt("false", 0)
	true = aInt("true", 1)
	
	def __init__(self, name, value):
		self.name = name
		self.value = value
		 
	
class aArray(aObject):
	def __init__(self, name):
		self.name = name
		self.value = []
		self.aType = "array"
		
class aError(aObject):
	def __init__(self, name):
		self.name = name
		self.aType = "error"
	def aRaise(self, text, ln):
		print("EXCEPTION: " + self.name + ": " + text + " on line " + str(ln) + "\n")
		input("Press enter to exit...\n")
		sys.exit()
		
		
class aPyInterface(aObject):
	pass
	
	
TypeErr = aError("TypeError")
		
		
def convertObject(obj, newType):
		try:
			if newType == "string":
				return aString(obj.name, str(obj.value))
		except TypeError:
			TypeErr.aRaise("Invalid Value For Object", "OBJ_DECLARE_" + obj.name)
			
		
		
