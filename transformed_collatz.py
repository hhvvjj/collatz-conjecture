#!/usr/bin/python3
####################################################################################################
# PoC for Collatz conjecture transformation
#
# J. Hernandez 2023
####################################################################################################

from tabulate import tabulate
from sympy.solvers import solve
from sympy import Symbol

# Returns Collatz value
def collatzValue(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1

# Returns n mod 2
def nModTwo(n):
    return n % 2

# Returns n mod 9
def nModNine(n):
    return n % 9

# Returns Collatz sequence
def buildCollatzSequence(n):
	collatzSequence = []
	collatzSequence.append(n)
	while n != 1:
		n = collatzValue(n)
		collatzSequence.append(n)
	return collatzSequence

# Returns a Essential Pair from a Collatz Pair
def computeEssentialPair(collatzPair):
	if nModNine(collatzPair[0]) == 0 and nModNine(collatzPair[1]) == 0:
		return [18,9]
	if nModNine(collatzPair[0]) == 0 and nModNine(collatzPair[1]) == 1:
		return [9,28]
	if nModNine(collatzPair[0]) == 1 and nModNine(collatzPair[1]) == 4:
		return [1,4]
	if nModNine(collatzPair[0]) == 1 and nModNine(collatzPair[1]) == 5:
		return [10,5]
	if nModNine(collatzPair[0]) == 2 and nModNine(collatzPair[1]) == 1:
		return [2,1]
	if nModNine(collatzPair[0]) == 2 and nModNine(collatzPair[1]) == 7:
		return [11,34]
	if nModNine(collatzPair[0]) == 3 and nModNine(collatzPair[1]) == 1:
		return [3,10]
	if nModNine(collatzPair[0]) == 3 and nModNine(collatzPair[1]) == 6:
		return [12,6]
	if nModNine(collatzPair[0]) == 4 and nModNine(collatzPair[1]) == 2:
		return [4,2]
	if nModNine(collatzPair[0]) == 4 and nModNine(collatzPair[1]) == 4:
		return [13,40]
	if nModNine(collatzPair[0]) == 5 and nModNine(collatzPair[1]) == 7:
		if nModTwo(collatzPair[0]) == 1:
			return [5,16]
		if nModTwo(collatzPair[0]) == 0:
			return [14,7]
	if nModNine(collatzPair[0]) == 6 and nModNine(collatzPair[1]) == 1:
		return [15,46]
	if nModNine(collatzPair[0]) == 6 and nModNine(collatzPair[1]) == 3:
		return [6,3]
	if nModNine(collatzPair[0]) == 7 and nModNine(collatzPair[1]) == 4:
		return [7,22]
	if nModNine(collatzPair[0]) == 7 and nModNine(collatzPair[1]) == 8:
		return [16,8]
	if nModNine(collatzPair[0]) == 8 and nModNine(collatzPair[1]) == 4:
		return [8,4]
	if nModNine(collatzPair[0]) == 8 and nModNine(collatzPair[1]) == 7:
		return [17,52]

# Returns a Generic Pair from a Collatz Pair
def computeGenericPair(collatzPair):
	if nModNine(collatzPair[0]) == 0 and nModNine(collatzPair[1]) == 0:
		return ['(3 * 3 * (1 * 2 * m + 0)) + 0', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 0']
	if nModNine(collatzPair[0]) == 0 and nModNine(collatzPair[1]) == 1:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 0', '(3 * 3 * 3 * (1 * 2 * m + 1)) + 1']
	if nModNine(collatzPair[0]) == 1 and nModNine(collatzPair[1]) == 4:
		return ['(3 * 3 * (1 * 2 * m + 0)) + 1', '(1 * 3 * 3 * (3 * 2 * m + 0)) + 4']
	if nModNine(collatzPair[0]) == 1 and nModNine(collatzPair[1]) == 5:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 1', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 5']
	if nModNine(collatzPair[0]) == 2 and nModNine(collatzPair[1]) == 1:
		return ['(3 * 3 * (1 * 2 * m + 0)) + 2', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 1']
	if nModNine(collatzPair[0]) == 2 and nModNine(collatzPair[1]) == 7:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 2', '(1 * 3 * 3 * (3 * 2 * m + 3)) + 7']
	if nModNine(collatzPair[0]) == 3 and nModNine(collatzPair[1]) == 1:
		return ['(1 * 3 * (3 * 2 * m + 0)) + 3', '(1 * 3 * 3 * (3 * 2 * m + 1)) + 1']
	if nModNine(collatzPair[0]) == 3 and nModNine(collatzPair[1]) == 6:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 3', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 6']
	if nModNine(collatzPair[0]) == 4 and nModNine(collatzPair[1]) == 2:
		return ['(3 * 3 * (1 * 2 * m + 0)) + 4', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 2']
	if nModNine(collatzPair[0]) == 4 and nModNine(collatzPair[1]) == 4:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 4', '(1 * 3 * 3 * (3 * 2 * m + 4)) + 4']
	if nModNine(collatzPair[0]) == 5 and nModNine(collatzPair[1]) == 7:
		if nModTwo(collatzPair[0]) == 1:
			return ['(3 * 3 * (1 * 2 * m + 0)) + 5', '(1 * 3 * 3 * (3 * 2 * m + 1)) + 7']
		if nModTwo(collatzPair[0]) == 0:
			return ['(3 * 3 * (1 * 2 * m + 1)) + 5', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 7']
	if nModNine(collatzPair[0]) == 6 and nModNine(collatzPair[1]) == 1:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 6', '(1 * 3 * 3 * (3 * 2 * m + 5)) + 1']
	if nModNine(collatzPair[0]) == 6 and nModNine(collatzPair[1]) == 3:
		return ['(3 * 3 * (1 * 2 * m + 0)) + 6', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 3']
	if nModNine(collatzPair[0]) == 7 and nModNine(collatzPair[1]) == 4:
		return ['(3 * 3 * (1 * 2 * m + 0)) + 7', '(1 * 3 * 3 * (3 * 2 * m + 2)) + 4']
	if nModNine(collatzPair[0]) == 7 and nModNine(collatzPair[1]) == 8:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 7', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 8']
	if nModNine(collatzPair[0]) == 8 and nModNine(collatzPair[1]) == 4:
		return ['(3 * 3 * (1 * 2 * m + 0)) + 8', '(1 * 3 * 3 * (1 * 1 * m + 0)) + 4']
	if nModNine(collatzPair[0]) == 8 and nModNine(collatzPair[1]) == 7:
		return ['(3 * 3 * (1 * 2 * m + 1)) + 8', '(1 * 3 * 3 * (3 * 2 * m + 5)) + 7']

# Returns a m multiplicity from a Collatz Pair
def computeMultiplicity(collatzPair):
	equation = computeGenericPair(collatzPair)
	m = Symbol('m')
	if solve(equation[0] + "-" + str(collatzPair[0])) == solve(equation[1] + "-" + str(collatzPair[1])):
		return solve(str(equation[0]) + "-" + str(collatzPair[0]))
	else:
		return -1

# FSM with 18 nodes to validate Collatz transformation
# Node q0 (initial node)
def nodeQ0(c):
	print("Digesting Transformed Representation:")
	switcher={
		210:'q1',
		420:'q2',
		630:'q3',
		140:'q4',
		141:'q4',
		840:'q4',
		7220:'q4',
		7221:'q4',
		13400:'q4',
		13401:'q4',
		1050:'q5',
		1260:'q6',
		1470:'q7',
		1680:'q8',
		1891:'q9',
		211:'q10',
		3100:'q10',
		3101:'q10',
		9280:'q10',
		9281:'q10',
		15460:'q10',
		15461:'q10',
		421:'q11',
		631:'q12',
		841:'q13',
		1051:'q14',
		1261:'q15',
		1471:'q16',
		5160:'q16',
		5161:'q16',
		11340:'q16',
		11341:'q16',
		17520:'q16',
		17521:'q16',
		1681:'q17',
		1890:'q18',

	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q0 with unexpected transition " + str(c))
		return None
	final = " "
	if (c == 210):
		final = " final "
	print("\t [+] From initial node q0 to" + final + "node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q1 (final node)
def nodeQ1(c):
	switcher={
		140:'q4',
		141:'q4',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q1 with unexpected transition " + str(c))
		return None
	print("\t [+] From final node q1 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q2
def nodeQ2(c):
	switcher={
		210:'q1',
		211:'q10',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q2 with unexpected transition " + str(c))
		return None
	final = " "
	if (c == 210):
		final = " final "
	print("\t [+] From node q12 to" + final + "node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q3
def nodeQ3(c):
	switcher={
		3100:'q10',
		3101:'q10',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q3 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q3 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q4
def nodeQ4(c):
	switcher={
		420:'q2',
		421:'q11',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q4 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q4 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q5
def nodeQ5(c):
	switcher={
		5160:'q16',
		5161:'q16',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q5 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q5 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q6
def nodeQ6(c):
	switcher={
		630:'q3',
		631:'q12',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q6 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q6 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q7
def nodeQ7(c):
	switcher={
		7220:'q4',
		7221:'q4',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q7 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q7 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q8
def nodeQ8(c):
	switcher={
		840:'q4',
		841:'q13',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q8 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q8 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q9
def nodeQ9(c):
	switcher={
		9280:'q10',
		9281:'q10',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q9 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q9 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q10
def nodeQ10(c):
	switcher={
		1050:'q5',
		1051:'q14',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q10 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q10 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q11
def nodeQ11(c):
	switcher={
		11340:'q16',
		11341:'q16',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q11 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q11 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q12
def nodeQ12(c):
	switcher={
		1260:'q6',
		1261:'q15',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q12 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q12 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q13
def nodeQ13(c):
	switcher={
		13400:'q4',
		13401:'q4',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q13 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q13 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q14
def nodeQ14(c):
	switcher={
		1470:'q7',
		1471:'q16',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q14 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q14 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q15
def nodeQ15(c):
	switcher={
		15460:'q10',
		15461:'q10',
	}	
	if (switcher.get(c) == None):
		print("\t\t [-] In node q15 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q15 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q16
def nodeQ16(c):
	switcher={
		1680:'q8',
		1681:'q17',
	}	
	if (switcher.get(c) == None):
		print("\t\t [-] In node q16 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q16 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q17
def nodeQ17(c):
	switcher={
		17520:'q16',
		17521:'q16',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q17 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q17 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Node q18
def nodeQ18(c):
	switcher={
		1890:'q18',
		1891:'q9',
	}	
	if (switcher.get(c) == None):
		print("\t [-] In node q18 with unexpected transition " + str(c))
		return None
	print("\t [+] From node q18 to node " + switcher.get(c) + " using transition " + str(c))
	return switcher.get(c)

# Returns boolean based on FSM acceptor
def isTransformedRepresentationAccepted(transformedCollatz): 
	n = len(transformedCollatz)
	i = 0
	fsmCurrentNode = "q0"
	while ((i <= n-1)):
		if (fsmCurrentNode == "q0"):
			fsmCurrentNode = nodeQ0(transformedCollatz[i])
		elif (fsmCurrentNode == "q1"): 
			fsmCurrentNode = nodeQ1(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q2"): 
			fsmCurrentNode = nodeQ2(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q3"): 
			fsmCurrentNode = nodeQ3(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q4"): 
			fsmCurrentNode = nodeQ4(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q5"): 
			fsmCurrentNode = nodeQ5(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q6"): 
			fsmCurrentNode = nodeQ6(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q7"): 
			fsmCurrentNode = nodeQ7(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q8"): 
			fsmCurrentNode = nodeQ8(transformedCollatz[i]) 
		elif (fsmCurrentNode == "q9"): 
			fsmCurrentNode = nodeQ9(transformedCollatz[i])
		elif (fsmCurrentNode == "q10"): 
			fsmCurrentNode = nodeQ10(transformedCollatz[i])
		elif (fsmCurrentNode == "q11"): 
			fsmCurrentNode = nodeQ11(transformedCollatz[i])
		elif (fsmCurrentNode == "q12"): 
			fsmCurrentNode = nodeQ12(transformedCollatz[i])
		elif (fsmCurrentNode == "q13"): 
			fsmCurrentNode = nodeQ13(transformedCollatz[i])
		elif (fsmCurrentNode == "q14"): 
			fsmCurrentNode = nodeQ14(transformedCollatz[i])
		elif (fsmCurrentNode == "q15"): 
			fsmCurrentNode = nodeQ15(transformedCollatz[i])
		elif (fsmCurrentNode == "q16"): 
			fsmCurrentNode = nodeQ16(transformedCollatz[i])
		elif (fsmCurrentNode == "q17"): 
			fsmCurrentNode = nodeQ17(transformedCollatz[i])
		elif (fsmCurrentNode == "q18"): 
			fsmCurrentNode = nodeQ18(transformedCollatz[i])
		else:
			return False
		i = i + 1
	print("")
	return True

# Returns sequence and its length
def printSequence(banner,sequence):
	print(banner, end="")
	for i in range(len(sequence)-1):
		print(sequence[i], end =", ")
	print(sequence[len(sequence)-1])
	printNewLine()
	print("Length of " + banner + str(len(sequence)))

# Returns a blank line
def printNewLine():
	print("")

# Main 
if __name__ == "__main__" : 

	n = int(input("Enter a value for n: "))

	printNewLine()

	collatzSequence = buildCollatzSequence(n)

	printSequence("Collatz Sequence: ", collatzSequence)

	printNewLine()

	resultsTable = []
	essentialPairSequence = []
	multiplicitiesSequence = []
	collatzTransformationSequence = []
	for i in range(len(collatzSequence)-1):
		collatzPair = [collatzSequence[i], collatzSequence[i+1]]
		essentialPair = computeEssentialPair([collatzSequence[i],collatzSequence[i+1]])
		genericPair = computeGenericPair(collatzPair)
		m = computeMultiplicity(collatzPair)
		multiplicitiesSequence.append(m[0])
		essentialPairSequence.append([essentialPair, m])
		collatzTransformationSequence.append(int(f"{essentialPair[0]}{essentialPair[1]}{nModTwo(m[0])}"))
		tableRow = [i+1, collatzPair, genericPair, essentialPair, m[0], nModTwo(m[0])]
		resultsTable.append(tableRow)

	print(tabulate(resultsTable, headers=["#", "Collatz Pairs", "Generic Pairs", "Essential Pairs", "Multiplicities m", "Multiplicities m mod 2"]))

	printNewLine()

	printSequence("Multiplicities Sequence: ", multiplicitiesSequence)

	printNewLine()

	printSequence("Collatz Transformation: ", collatzTransformationSequence)

	printNewLine()

	if (isTransformedRepresentationAccepted(collatzTransformationSequence)) :
		print("Transformed Representation for n = " + str(n) + " IS ACCEPTED") 
	else:
		print("Transformed Representation for n = " + str(n) + " IS NOT ACCEPTED") 
