import classes

def out(value):
	print(value)

def defaultStreamf(value):
	pass

SyntaxErr = classes.aError("SyntaxError")

InternalErr = classes.aError("InternalError")

ImportErr = classes.aError("ImportError")

TypeErr = classes.aError("TypeError")

NameErr = classes.aError("NameError")

defaultStream = classes.aStream("stream_obj", defaultStreamf)

aStdout = classes.aStream("stdout", out)
