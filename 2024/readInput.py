def yieldLines(filename):
	with open(f'inputs/{filename}', 'r') as f:
		for line in f:
			yield line

def linesToList(filename):
	with open(f'inputs/{filename}', 'r') as f:
		lines = f.readlines()
		lines = [line.strip() for line in lines]
		return lines

def oneString(filename):
	with open(f'inputs/{filename}', 'r') as f:
		return f.read()