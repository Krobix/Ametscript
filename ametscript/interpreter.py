import classes
import abuiltins
import io
import sys
import traceback
import ametconfig as config
import pathlib
import threading

version = "0.4.1"

tmpValueGet = 0

ln = 0

lastLn = ""

typeKeywords = [
	"num",
	"string",
	"bool",
	"point",
	"stream"]
	
declarationKeywords = [
	"func",
	"class",
	"var",
	"dynamic",
	"public",
	"private",
	"protected"]
	
quoteSymbols = ["'", '"']

lastValue = ["", "", ""]

mathSymbols = ["+",
	"-",
	"/",
	"*",
	"**",
]


	
variables = {
	"__CTX__": classes.aString("__CTX__", "main"),
	"SyntaxError": abuiltins.SyntaxErr,
	"InternalError": abuiltins.InternalErr,
	"ImportError": abuiltins.ImportErr,
	"true": classes.aBool.true,
	"false": classes.aBool.false,
	"TypeError": classes.TypeErr,
	"NameError": abuiltins.NameErr,
	"stdout": abuiltins.aStdout,
}

extTypes = {
	"stream":abuiltins.defaultStream,
}

def copyList(list1, list2):
	l = len(list2)
	temp = 0
	while len(list1) > l:
		list2.append(list1[temp])
		temp = temp + 1
	return list2
			
			
def eval_expr(expr):
	global variables, mathSymbols
	for x in variables:
		while "<" + x + ">" in expr:
			expr = expr.replace("<" + variables[x].name + ">", "\"" + str(variables[x].value) + "\"") 
	try:
		return eval(expr)
	except SyntaxError:
		abuiltins.SyntaxErr.aRaise("Invalid expression: " + expr, ln)
	except NameError:
		abuiltins.NameErr.aRaise("Unknown Variable referenced", ln)
		 
def defVar(inp, context):
	ctx = context
	a = {}
	exprStart = inp.index("=") + 1
	if ctx.value == "main":
		if len(inp) >= 3:
			if not inp[0] in declarationKeywords + typeKeywords and inp[0] in variables:
				variables[inp[0]].value = eval_expr("".join(inp[exprStart:]))
				return None
			else:
				equalsIndex = inp.index("=")
				newName = inp[equalsIndex - 1]
		expression = inp[exprStart:]
		newVal = eval_expr(" ".join(expression)) 		
		variables[newName] = classes.aObject(newName, newVal, "Object")
		variables[newName] = classes.convertObject(variables[newName], inp[0], ln, attr=a)
		lastValue[0] = newName
		lastValue[1] = variables[newName].value
				
				
def exec_line(inp):
	global ln, lastLn
	lineLen = len(inp) - 1
	lastLn = " ".join(inp)
	if len(inp) == 0:
		return None
	elif inp[0] in typeKeywords or inp[0] in variables:
			if inp[1] == "var" or inp[0] in variables:
				defVar(inp, variables["__CTX__"])
	elif inp[0] == "import":
		importedFile = inp[1] + ".amts"
		modPath = pathlib.Path(config.globalModDir)
		try:
			file = modPath / importedFile
			with file.open('r', encoding='utf-8') as f:
				content = f.read()
				content = content.split(";")
				for x in content:
					ln = str(int(str(ln).split(" ")[0]) + 1) + " in " + importedFile
					x = list(x)
					if "\n" in x:
						x.remove("\n")
					exec_line("".join(x).split(" "))
				ln = 0
		except FileNotFoundError:
			abuiltins.ImportErr.aRaise("The module " + inp[1] + " does not exist.", ln)
	elif "".join(inp).startswith("//"):
		pass
	elif inp[0] == "\n" or inp[0] == " " or inp[0] == "":
		inp.remove(inp[0])
		exec_line(inp)					
	
	else:
		abuiltins.SyntaxErr.aRaise("Invalid Syntax", ln)

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
		abuiltins.InternalErr.aRaise(buffer.getvalue(), ln)
		
					 
