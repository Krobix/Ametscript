import classes
import abuiltins
import io
import sys
import traceback

version = "0.2.1"

typeKeywords = [
	"int",
	"string",
	"bool",
	"point",
	"float"]
	
declarationKeywords = [
	"func",
	"class",
	"var",
	"dynamic",
	"public",
	"private",
	"protected"]
	
quoteSymbols = ["'", '"']

lastValue = ["", ""]
	
variables = {
	"__CTX__": classes.aString("__CTX__", "main")
}

def copyList(list1, list2):
	l = len(list2)
	temp = 0
	while len(list1) > l:
		list2.append(list1[temp])
		temp = temp + 1
	return list2
	
def getValue(expr):
	try:
		return int(eval(expr))
	except:
		if expr in variables:
			return variables[expr]
		elif list(expr)[0] in quoteSymbols and list(expr)[len(list(expr)) - 1] == list(expr[0]):
			for x in list(expr):
				if quoteSymbols[0] == list(expr[list(expr).index(x)]) or quoteSymbols[1] == list(expr[list(expr).index(x)]):
					temp = list(expr)
					temp.remove(x)
			return temp
					
				
	
def defVar(inp, context):
	ctx = context
	newVal = list(inp[len(inp) - 1])
	if ctx.value == "main":
		if len(inp) >= 3:
			if not inp[0] in declarationKeywords + typeKeywords and inp[0] in variables:
				newName = inp[0]
			else:
				equalsIndex = inp.index("=")
				newName = inp[equalsIndex - 1]
				if (quoteSymbols[1] in newVal or quoteSymbols[0] in newVal) and newVal[0] == newVal[len(newVal)-1]: 
					variables[newName] = classes.aObject(newName, inp[len(inp) - 1], "BASE_OBJ")
				elif inp[len(inp) - 1] in variables:
					variables[newName] = classes.aObject(newName, variables[inp[len(inp) - 1]], "BASE_OBJ")
		variables[newName] = classes.convertObject(variables[newName], inp[0])
		lastValue[0] = newName
		lastValue[1] = variables[newName].value
				
				
def exec_line(inp):
	lineLen = len(inp) - 1
	if inp[0] in typeKeywords:
			if inp[1] == "var":
				defVar(inp, variables["__CTX__"])
				
	else:
		abuiltins.SyntaxErr.aRaise("Invalid Syntax", 0)

def run():
	while True:
		inp = input(">>")
		print("\n")
		inp = inp.split(" ")
		exec_line(inp)
		
		
if __name__ == "__main__":
	print("Ametscript interpreter version " + version + "\n")
	
	try:
		run()
	except:
		oldS = sys.stdout
		sys.stdout = buffer = io.StringIO()
		traceback.print_exc()
		sys.stdout = oldS
		abuiltins.InternalErr.aRaise(buffer.getvalue(), 0)
		
					 
