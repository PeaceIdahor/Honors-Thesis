import sys
#-------------------------Importing Helper Functions --------------------------------------------------------------------------------------------------------------------
from thesisfunctions import verilogFuncs
from thesisfunctions import prepareDot
import os
import re 
operationsA = []
"""
This returnOut function does most of the translating of the verilog. It is a recursive function that receives as 
inputs,
Array:  An array containing the operation performed in the assign statement
indexMaster: A number used to differenciate between different operations of the same type
outputE: the result of the strip function showing what the output of the returnOut function should look like
outputN: the variable the output of the assign statement is assigned to
"""
def returnOut(Array,indexMaster,outputE,outputN=""):
	if len(Array) == 1:
		for indexItem,items in enumerate(operationsA):
			if items[2] == Array[0]:
				operationsA[indexItem][2] = outputN
				outputA.append(outputN)
				outputA.remove(Array[0])
	if "(" in Array:
		openind = []
		closeind = []
		for index,item in enumerate(Array):
			if item =="(":
				openind.append(index)
			if item ==")":
				closeind.append(index)
		i = len(openind)
		while((i - len(openind))<=i):
			indexMaster +=1
			if "(" in Array:
				sig = 0
				lp = openind[len(openind)-1]
				rp = closeind[0]
				rightSide = Array[lp+1:rp]
			else:
				sig = 1
				rightSide = Array
			operationin,Array2,out = returnOut(rightSide,indexMaster,outputE,outputN)
			bufferA.append(out)
			if sig == 0:
				while rp >= lp:
					Array.pop(rp)
					rp -=1
				Array.insert(lp,out)
			openind = []
			closeind = []
			for index,item in enumerate(Array):
				if item =="(":
					openind.append(index)
				if item ==")":
					closeind.append(index)
			if len(openind)==0 and len(Array) !=1 :
				for item in Array:
					if item == "&" or item == "|" or item =="^":
						indexMaster +=1
						lp = Array.index(item)-1
						rp = Array.index(item)+2
						rightSide = Array[lp:rp]
						operationin,Array2,out = returnOut(rightSide,indexMaster,outputE,outputN)
						rp2 = rp-1
						while (rp2) >= lp:
							Array.pop(rp2)
							rp2 -=1
						Array.insert(lp,out)
			if out == outputE:
				bufferA.remove(out)
				#outputA.append(out)
				#operationsA.append([operationin,Array2,outputN])
				return out
			
	else:
		if "&" in Array and "~" not in Array:
			operationin = "And" + f"/{indexMaster}"
			out= f"{Array[0]}" + "&" + f"{Array[2]}"
			inputA.append(Array[0])
			if Array[0] in outputA:
				bufferA.append(Array[0])
			inputA.append(Array[2])
			if Array[2] in outputA:
				bufferA.append(Array[2])
			Array.pop(Array.index("&"))
			bufferA.append(out)
			if out == outputE:
				outputA.append(outputN)
				operationsA.append([operationin,Array,outputN])
			else:
				operationsA.append([operationin,Array,out])
			return operationin,Array,out
		if "|" in Array and "~" not in Array:
			operationin = "or" + f"/{indexMaster}"
			out= f"{Array[0]}" + "|" + f"{Array[2]}"
			inputA.append(Array[0])
			if Array[0] in outputA:
				bufferA.append(Array[0])
			inputA.append(Array[2])
			if Array[2] in outputA:
				bufferA.append(Array[2])
			Array.pop(Array.index("|"))
			bufferA.append(out)
			if out == outputE:
				outputA.append(outputN)
				operationsA.append([operationin,Array,outputN])
			else:
				operationsA.append([operationin,Array,out])
			return operationin,Array,out
		if "^" in Array and "~" not in Array:
			operationin = "xor" + f"/{indexMaster}"
			out= f"{Array[0]}" + "^" + f"{Array[2]}"
			inputA.append(Array[0])
			if Array[0] in outputA:
				bufferA.append(Array[0])
			inputA.append(Array[2])
			if Array[2] in outputA:
				bufferA.append(Array[2])
			Array.pop(Array.index("^"))
			bufferA.append(out)
			if out == outputE:
				outputA.append(outputN)
				operationsA.append([operationin,Array,outputN])
			else:
				operationsA.append([operationin,Array,out])
			return operationin,Array,out	
		if "~" in Array:
			operationin = "not" + f"/{indexMaster}"
			indexMaster +=1
			indexV = Array[Array.index("~")+1]
			Arrayin = [indexV]
			out= "~" + f"{indexV}"
			if out in bufferA:
				operationin = notTrack[out]
			else:
				bufferA.append(out)
				notTrack[out] = operationin 
			notDict.append([out,indexMaster])
			inputA.append(indexV)
			if indexV in outputA:
				bufferA.append(indexV)
			Array.pop(Array.index("~"))
			"""
			Trying to fix the bug where multiple lines are created to a node
			"""
			operationsA.append([operationin,Arrayin,out])
			if len(Array) >1:
				#bufferA.append(out)
				indexf = Array.index(indexV)
				Array.pop(indexf)
				Array.insert(indexf,out)
				out = returnOut(Array,indexMaster,outputE,outputN)
				return out
			if out == outputE:
				outputA.append(outputN)
				operationsA.append([operationin,Array,outputN])
			else:
				operationsA.append([operationin,Array,out])
			return operationin,Array,out	
		if "~&"	 in Array:
			operationin = "Nand" + f"/{indexMaster}"
			out= f"{Array[0]}" + "~&" + f"{Array[2]}"
			inputA.append(Array[0])
			if Array[0] in outputA:
				bufferA.append(Array[0])
			inputA.append(Array[2])
			if Array[2] in outputA:
				bufferA.append(Array[2])
			Array.pop(Array.index("~&"))
			bufferA.append(out)
			if out == outputE:
				outputA.append(outputN)
				operationsA.append([operationin,Array,outputN])
			else:
				operationsA.append([operationin,Array,out])
			return operationin,Array,out		
		if "~|" in Array:
			operationin = "Nor" + f"/{indexMaster}"
			out= f"{Array[0]}" + "~|" + f"{Array[2]}"
			inputA.append(Array[0])
			if Array[0] in outputA:
				bufferA.append(Array[0])
			inputA.append(Array[2])
			if Array[2] in outputA:
				bufferA.append(Array[2])
			Array.pop(Array.index("~|"))
			bufferA.append(out)
			if out == outputE:
				outputA.append(outputN)
				operationsA.append([operationin,Array,outputN])
			else:
				operationsA.append([operationin,Array,out])
			return operationin,Array,out	
		if "~^" in Array:
			operationin = "Xnor" + f"/{indexMaster}"
			out= f"{Array[0]}" + "~^" + f"{Array[2]}"
			inputA.append(Array[0])
			if Array[0] in outputA:
				bufferA.append(Array[0])
			inputA.append(Array[2])
			if Array[2] in outputA:
				bufferA.append(Array[2])
			Array.pop(Array.index("~^"))
			bufferA.append(out)
			if out == outputE:
				outputA.append(outputN)
				operationsA.append([operationin,Array,outputN])
			else:
				operationsA.append([operationin,Array,out])
			return operationin,Array,out
"""
This function gives an initial view of the resulting output of each assign statement in it's simplest form
So given an assign statement such as
assign c = b & f;
the strip function returns b&f
"""
def strip(array):
	while "(" in array:
		array.remove("(")
	while ")" in array:
		array.remove(")")
	return ''.join(array)
def returnOutB(array):
	operation = array[0].split('/')[0]
	operationIndex = array[0].split('/')[1]
	for key in libDict:
		if key == operation:
			expr = libDict[key]
			expr = expr.replace('*', '&').replace('+', '|').replace('!', '~')
			expr = expr[2:]
			for i in range(len(expr)-1):
				if expr[i] == "|" or expr[i] =="&" or expr[i] == "^" :
					if (expr[i-2] !="(" or expr[i+2] != ")") and 2+i != len(expr)-1:
						exprlist = re.findall(r'\(|\)|[~&\|]|[\w_]+',expr)
						exprlist.insert(i-1,"(")
						exprlist.insert(i+3,")")
						expr = ''.join(exprlist)
			for item in array[1]:
				for key in varDict:
					if key.split("/")[1] == operationIndex:
						if varDict[key] == item:
							key = key.split("/")[0]
							expr = expr.replace(key[1:],item)
	outputE = strip(list(expr))
	outputN = array[2]
	exprinput = re.findall(r'\(|\)|[~&\|]|[\w_]+',expr)
	returnOut(exprinput,int(operationIndex),outputE,outputN)
	return
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if sys.argv[1]== 'G':
	lib = sys.argv[2]
	f = sys.argv[3]
	inputs = []
	regs = []
	outputs = []
	wires = []


	wordArrsave = verilogFuncs.parser(f)
	wordArrsave2 = verilogFuncs.parser2(lib)
	dotFile = open("Translate.dot","a")
	dotfile = prepareDot(dotFile)
	dotfile.openDot()#opening a dot file
	numberOfClauses = 0
	numberOfVariables = 0
	libDict = {}
	varDict = {}
	clauses = []
	inputA = []
	outputA = []
	bufferA = []
	varsA = []
	notDict = []
	notTrack = {}
	inputPrimary = []
	for index,word in enumerate(wordArrsave2):
		if word == "GATE":
			libDict[wordArrsave2[index+1]] = wordArrsave2[index+3]
	for index, word in enumerate(wordArrsave):
		if word == "//": # checking to see if part of the code was commented 
			while wordArrsave[index] != ";":
				wordArrsave.pop(index)
		if word == "input" or word == "output" or word == "wire" or word == "reg":
			index2 = index + 1
			while wordArrsave[index2] != ";":
				varsA.append(wordArrsave[index2])
				index2 += 1
		if word == "input":
			indexInput = index +1
			while wordArrsave[indexInput] != ";":
				inputPrimary.append(wordArrsave[indexInput])
				indexInput +=1
		for key in libDict:
			if key == word:
				line = []
				index2 = index
				while wordArrsave[index2] != ";":
					if '.' in wordArrsave[index2]:
						varDict[wordArrsave[index2] + f'/{index}'] = wordArrsave[index2+1]
					else:
						line.append(wordArrsave[index2])
					index2 +=1
				for item in line[2:-1]:
					inputA.append(item)
				outputA.append(line[len(line)-1])
				name = line[0]+f'/{index}'
				clauses.append([name,line[2:-1],line[len(line)-1]])

	val = input("High Abstraction on ? [y/n] :")
	if val == "y" or val == "Y":
		Abst = 1
		print("High Abstraction on")
	elif val == "n" or val == "N":
		Abst=0
		print("High Abstraction off")
	else:
		raise Exception("Sorry Y or N only")
	if Abst == 1:
		for array in clauses:
			for item in array[1]:
				if item in outputA:
					bufferA.append(item)
		dotfile.setup(inputA,bufferA,outputA)
		verilogFuncs.processVisual(bufferA,clauses,inputA)
		val = input("Debug mode on ? [y/n] :")

		if val == "y" or val == "Y":
			labelon = 1
			print("Debug Mode on")
		elif val == "n" or val == "N":
			labelon=0
			print("Debug Mode off")
		else:
			raise Exception("Sorry Y or N only")
		inputSpecifiedArray = {}
		specifyInputs = input("Specifying inputs? [y/n] :")
		if specifyInputs == "y" or specifyInputs == "Y":
			inputon = 1
			for item in inputPrimary:
				inputSpecified = input(f"{item}: ")
				if inputSpecified =="0" or inputSpecified == "1":
					inputSpecifiedArray[item] = inputSpecified
				else:
					raise Exception("Input must be 0 or 1")
		elif specifyInputs == "n" or specifyInputs == "N":
			inputon = 0
		else:
			raise Exception("Sorry Y or N only")
		if inputon ==1:
			for array in clauses:
				returnOutB(array)
			verilogFuncs.simulation(operationsA,inputSpecifiedArray)
			for index, array1 in enumerate(clauses):
				for array2 in operationsA:
					if array1[2] == array2[2]:
						clauses[index].append([])
						clauses[index].append([])
						clauses[index][4] = array2[4]
			for index, array in enumerate(clauses):
				for item in array[1]:
					clauses[index][3].append(0)
			for index1, array1 in enumerate(clauses):
				for index2, array2 in enumerate(operationsA):
					for item in array1[1]:
						if item in array2[1]:
							clauses[index1][3][array1[1].index(item)] = array2[3][array2[1].index(item)]
		verilogFuncs.writeVisuals(dotFile,clauses,bufferA,labelon,inputon)
		dotfile.endFile() #closing the dotfile
	else:
		for array in clauses:
			returnOutB(array)
		dotfile.setup(inputA,bufferA,outputA)
		verilogFuncs.processVisual(bufferA,operationsA,inputA)
		val = input("Debug mode on ? [y/n] :")

		if val == "y" or val == "Y":
			labelon = 1
			print("Debug Mode on")
		elif val == "n" or val == "N":
			labelon=0
			print("Debug Mode off")
		else:
			raise Exception("Sorry Y or N only")
		inputSpecifiedArray = {}
		specifyInputs = input("Specifying inputs? [y/n] :")
		if specifyInputs == "y" or specifyInputs == "Y":
			inputon = 1
			for item in inputPrimary:
				inputSpecified = input(f"{item}: ")
				if inputSpecified =="0" or inputSpecified == "1":
					inputSpecifiedArray[item] = inputSpecified
				else:
					raise Exception("Input must be 0 or 1")
		elif specifyInputs == "n" or specifyInputs == "N":
			inputon = 0
		else:
			raise Exception("Sorry Y or N only")
		if inputon ==1:
			verilogFuncs.simulation(operationsA,inputSpecifiedArray)
		verilogFuncs.writeVisuals(dotFile,operationsA,bufferA,labelon,inputon)
		dotfile.endFile() #closing the dotfile

elif sys.argv[1] == 'B':
	
	f = sys.argv[2]
	wordArrsave = verilogFuncs.parser3(f) #extracting important information from my verilog file
	dotFile = open("Translate.dot","a")
	dotfile = prepareDot(dotFile)
	dotfile.openDot()#opening a dot file

	#outputA,outinA,bufferA,buffinA,inputA,inpinA = verilogFuncs.populateA(wordArrsave)
	inputA = []
	inputPrimary = []
	bufferA = [] #buffer array containing the intermediates values that are not inputs or outputs
	outputA = []
	operationsA = [] #array containing all the operations and the inputs and outputs to those operations
	notDict = []
	notTrack = {}

	"""
	This returnOut function does most of the translating of the verilog. It is a recursive function that receives as 
	inputs,
	Array:  An array containing the operation performed in the assign statement
	indexMaster: A number used to differenciate between different operations of the same type
	outputE: the result of the strip function showing what the output of the returnOut function should look like
	outputN: the variable the output of the assign statement is assigned to
	"""

	"""
	This for loop is used to search for assign statements and then call the returnOut function with the previously 
	specified perameters.
	It also ignores any commented lined in the verilog script.
	You can comment lines of verilog, but you cannot add commented lines that are not verilog
	"""
	for index,word in enumerate(wordArrsave):
		if word =="//": #checking to see if part of the code was commented 
			while wordArrsave[index] !=";":
				wordArrsave.pop(index)
		rightSide=[]
		if word == "assign": # the only part I care about are the assign statements
			indexMaster = index #get the index of the assign statement
			index2=index+3
			outputN = wordArrsave[index + 1]
			while wordArrsave[index2] != ";": #getting the rightside of the assign statement
				rightSide.append(wordArrsave[index2])
				index2 +=1
			rightside2 = rightSide.copy()
			outputE = strip(rightside2)
			Array = returnOut(rightSide,indexMaster,outputE,outputN)
		if word == "input":
			indexInput = index +1
			while wordArrsave[indexInput] != ";":
				inputPrimary.append(wordArrsave[indexInput])
				indexInput +=1
			#returnOut(Array,indexMaster)

	#checking to see if the visual representation is in debug mode or not
	val = input("Debug mode on ? [y/n] :")

	if val == "y" or val == "Y":
		labelon = 1
		print("Debug Mode on")
	elif val == "n" or val == "N":
		labelon=0
		print("Debug Mode off")
	else:
		raise Exception("Sorry Y or N only")

	#getting actual inputs from the user in terms of 0 or 1
	inputSpecifiedArray = {}
	specifyInputs = input("Specifying inputs? [y/n] :")
	if specifyInputs == "y" or specifyInputs == "Y":
		inputon = 1
		for item in inputPrimary:
			inputSpecified = input(f"{item}: ")
			if inputSpecified =="0" or inputSpecified == "1":
				inputSpecifiedArray[item] = inputSpecified
			else:
				raise Exception("Input must be 0 or 1")
	elif specifyInputs == "n" or specifyInputs == "N":
		inputon = 0
	else:
		raise Exception("Sorry Y or N only")
	dotfile.setup(inputA,bufferA,outputA)
	#calling the visual representation functions that write to the dot file
	verilogFuncs.processVisual(bufferA,operationsA,inputA)
	if inputon ==1:
		verilogFuncs.simulation(operationsA,inputSpecifiedArray)
	operationsDict = {}
	verilogFuncs.writeVisuals(dotFile,operationsA,bufferA,labelon,inputon)
	dotfile.endFile() #closing the dotfile
else:
	raise Exception("Sorry Boolean or Gate level verilog only")