import itertools

while (True):
	try:
		k = raw_input()
		list(k)
		permutations = list(set(itertools.permutations(k)))
		sortedpermutations = sorted(permutations)[::-1]
		for element in sortedpermutations:
			number = int("".join(element))
			print number
	except EOFError:
		break
