def yieldLines(filename):
	with open(f'inputs/{filename}', 'r') as f:
		for line in f:
			yield line

def linesToList(filename):
	with open(f'inputs/{filename}', 'r') as f:
		return f.readlines()