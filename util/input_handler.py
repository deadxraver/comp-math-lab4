file = None

def setfile(file_name):
	global file
	file = open(file_name, "r")

def read(prompt=''):
	if file is None:
		return input(prompt)
	else:
		return file.readline()