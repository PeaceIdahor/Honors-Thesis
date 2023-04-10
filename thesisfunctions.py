class verilogFuncs:
    def  parser(file): #function to parse the verilog file to create a word array

            wordArr = [] #an array of characters that appear in sequence
            wordArrsave = []
            count = 0
            index = 0
            with open(file, 'r') as f:
                for line in f:
                    for word in line:
                        if word == ' ' or word == '\n' or word == '	' or word==',' or word=="(" or word==")": #creating a line of demarkation to seperate characters in sequence
                            command = ''.join(wordArr) #joining those characters into a str word that represents some kind of command
                            check = 0
                            if ';' in command and len(command)>1:
                                check =1
                                if command in wordArrsave:
                                    wordArrsave.remove(command)
                                    index -=1
                                command = command.replace(';',"")
                                wordArrsave.append(command)
                                if wordArrsave[index-1] !=None and wordArrsave[index-1] == ")":
                                    wordArrsave[index] = ")"
                                    wordArrsave[index-1]=command
                                index+=1
                                wordArrsave.append(';')
                                index+=1
                            if check == 0:
                                wordArrsave.append(command) #appending that command to my list of words that I will refer back to later
                                index +=1
                            wordArr = []
                            count +=1
                        else:
                            wordArr.append(word)

            #-----------------------Preparing the command array to leave only relevant information from the verilog file ----------------------------------------
            while '' in wordArrsave: #removing empty strings from the list
                wordArrsave.remove('')
            return wordArrsave
    def parser2(file):
            wordArr = [] #an array of characters that appear in sequence
            wordArrsave = []
            count = 0
            index = 0
            with open(file, 'r') as f:
                for line in f:
                    for word in line:
                        if word == ' ' or word == '\n' or word == '	' or word==',': #creating a line of demarkation to seperate characters in sequence
                            command = ''.join(wordArr) #joining those characters into a str word that represents some kind of command
                            check = 0
                            if ';' in command and len(command)>1:
                                check =1
                                if command in wordArrsave:
                                    wordArrsave.remove(command)
                                    index -=1
                                command = command.replace(';',"")
                                wordArrsave.append(command)
                                if wordArrsave[index-1] !=None and wordArrsave[index-1] == ")":
                                    wordArrsave[index] = ")"
                                    wordArrsave[index-1]=command
                                index+=1
                                wordArrsave.append(';')
                                index+=1
                            if check == 0:
                                wordArrsave.append(command) #appending that command to my list of words that I will refer back to later
                                index +=1
                            wordArr = []
                            count +=1
                        else:
                            wordArr.append(word)

            #-----------------------Preparing the command array to leave only relevant information from the verilog file ----------------------------------------
            while '' in wordArrsave: #removing empty strings from the list
                wordArrsave.remove('')
            return wordArrsave   
    def  parser3(file): #function to parse the verilog file to create a word array
        wordArr = [] #an array of characters that appear in sequence
        wordArrsave = []
        count = 0
        index = 0
        with open(file, 'r') as f:
            for line in f:
                for word in line:
                    if word == ' ' or word == '\n' or word == '	' or word==',': #creating a line of demarkation to seperate characters in sequence
                        command = ''.join(wordArr) #joining those characters into a str word that represents some kind of command
                        check = 0
                        if "~" in command:
                            check = 1
                            if command in wordArrsave:
                                wordArrsave.remove(command)
                                index -=1
                            command = command.replace('~',"")
                            wordArrsave.append('~')
                            index+=1
                            wordArrsave.append(command)
                            index+=1
                        if '(' in command:
                            check = 1
                            if command in wordArrsave:
                                wordArrsave.remove(command)
                                index -=1
                            command = command.replace('(',"")
                            wordArrsave.append('(')
                            index+=1
                            wordArrsave.append(command)
                            index+=1
                        if '!' in command:
                            check = 1
                            if command in wordArrsave:
                                wordArrsave.remove(command)
                                index -=1
                            command = command.replace('!',"")
                            wordArrsave.append('!')
                            index+=1
                            wordArrsave.append(command)
                            index+=1
                        if '//' in command:
                            check =1
                            if command in wordArrsave:
                                wordArrsave.remove(command)
                                index -=1
                            command = command.replace('//',"")
                            wordArrsave.append('//')
                            index +=1
                            wordArrsave.append(command)
                            index +=1
                        if ')' in command:
                            check =1
                            if command in wordArrsave:
                                wordArrsave.remove(command)
                                index -=1
                            command = command.replace(')',"")
                            wordArrsave.append(command)
                            index +=1
                            wordArrsave.append(')')
                            index +=1
                        if ';' in command:
                            check =1
                            if command in wordArrsave:
                                wordArrsave.remove(command)
                                index -=1
                            command = command.replace(';',"")
                            wordArrsave.append(command)
                            if wordArrsave[index-1] !=None and wordArrsave[index-1] == ")":
                                wordArrsave[index] = ")"
                                wordArrsave[index-1]=command
                            index+=1
                            wordArrsave.append(';')
                            index+=1

                        if check == 0:
                            wordArrsave.append(command) #appending that command to my list of words that I will refer back to later
                            index +=1
                        wordArr = []
                        count +=1
                    else:
                        wordArr.append(word)

        #-----------------------Preparing the command array to leave only relevant information from the verilog file ----------------------------------------
        while '' in wordArrsave: #removing empty strings from the list
            wordArrsave.remove('')
        return wordArrsave
    def processVisual(bufferA,operationsA,inputA):
        for index,item in enumerate(bufferA):
            if "(" in item:
                bufferA[index] = item.replace("(","")
            if ")" in item:
                bufferA[index]= item.replace(")","")
        for index,item in enumerate(inputA):
            if "(" in item:
                inputA[index] = item.replace("(","")
            if ")" in item:
                inputA[index]= item.replace(")","")
        for index1, arrays in enumerate(operationsA):
            for index2,items in enumerate(arrays):
                if isinstance(items,list):
                    for index3,item in enumerate(items):
                        if "(" in item:
                            operationsA[index1][index2][index3] = item.replace("(","")
                        if ")" in item:
                            operationsA[index1][index2][index3] = item.replace(")","")
                else:
                    if "(" in items:
                        arrays[index2] = items.replace("(","")
                    if ")" in items:
                        arrays[index2] = items.replace(")","")       
    def writeVisuals(fDot,operationsA,bufferA,labelon,inputon):
        savedArr = []
        dotfile = prepareDot(fDot)
        for arrays in operationsA:
            if arrays[0][:3] == "inv" or arrays[0][:3] == "not":
                dotfile.writeNode(arrays[0],"circle")
            else:
                dotfile.writeNode(arrays[0],"oval")
            if arrays[2] not in bufferA:
                dotfile.writeNode(arrays[2],"triangle")
            for items in arrays[1]:
                if items not in bufferA:
                    dotfile.writeNode(items,"invtriangle")
        for index,arrays in enumerate(operationsA):
            for index2, items in enumerate(arrays[1]):
                if items in bufferA:
                    for itemx in operationsA:
                        if itemx[2] == items:
                            if labelon ==1 :
                                if f"{itemx[0],arrays[0],items}" not in savedArr:
                                    savedArr.append(f"{itemx[0],arrays[0],items}")
                                    dotfile.writeEdgeNode(itemx[0],arrays[0],items)
                            if labelon == 0 and inputon == 0:
                                if f"{itemx[0],arrays[0]}" not in savedArr:
                                    savedArr.append(f"{itemx[0],arrays[0]}")
                                    dotfile.writeEdgeNode(itemx[0],arrays[0])
                            if inputon == 1 and labelon == 0:
                                if f"{itemx[0],arrays[0],items}" not in savedArr:
                                    savedArr.append(f"{itemx[0],arrays[0],items}")
                                    dotfile.writeEdgeNode(itemx[0],arrays[0],operationsA[index][3][arrays[1].index(items)])
                else:
                    if f"{items[0],arrays[0]}" not in savedArr and inputon==1:
                        savedArr.append(f"{items[0],arrays[0]}")
                        dotfile.writeEdgeNode(items,arrays[0],operationsA[index][3][index2])
                    elif f"{items[0],arrays[0]}" not in savedArr and inputon==0:
                        savedArr.append(f"{items[0],arrays[0]}")
                        dotfile.writeEdgeNode(items,arrays[0])
            if arrays[2] not in bufferA:
                if f"{arrays[0],arrays[2]}" and inputon == 1:
                    dotfile.writeEdgeNode(arrays[0],arrays[2],operationsA[index][4][0])
                elif f"{arrays[0],arrays[2]}" and inputon == 0:
                    dotfile.writeEdgeNode(arrays[0],arrays[2])
    def andGate(inputA,inputB):
        return str(int(inputA)*int(inputB))
    def simulation(operationsA, inputSpecifiedArray):
        for index1,items in enumerate(operationsA):
            operationsA[index1].append([])
            operationsA[index1].append([])
            for inputs in items[1]:
                for key in inputSpecifiedArray:
                    if inputs == key:
                        operationsA[index1][3].append(inputSpecifiedArray[key])
                        if operationsA[index1][0][0] == "A" and len(operationsA[index1][3])>1:
                            inputSpecifiedArray[operationsA[index1][2]] = simulationInput.and_gate(operationsA[index1][3][0],operationsA[index1][3][1])
                            operationsA[index1][4].append(inputSpecifiedArray[operationsA[index1][2]])
                            break
                        if operationsA[index1][0][0] == "n":
                            inputSpecifiedArray[operationsA[index1][2]] = simulationInput.not_gate(operationsA[index1][3][0])
                            operationsA[index1][4].append(inputSpecifiedArray[operationsA[index1][2]])
                            break
                        if operationsA[index1][0][0] == "o" and len(operationsA[index1][3])>1:
                            inputSpecifiedArray[operationsA[index1][2]] = simulationInput.or_gate(operationsA[index1][3][0],operationsA[index1][3][1])
                            operationsA[index1][4].append(inputSpecifiedArray[operationsA[index1][2]])
                            break

class prepareDot:
    def __init__(self,fDot):
        self.fDot = fDot
    def openDot(self):
        self.fDot.truncate(0)
        self.fDot.write("digraph test{\n")
    def setup(self,inputA,bufferA,outputA): #function to prepare dot file
        #fDot.write('splines="ortho"\n')
        self.fDot.write('subgraph inputs{ rank="same"')
        for item in inputA:
            if item not in bufferA:
                if "(" in item:
                    item = item.replace("(","")
                if ")" in item:
                    item = item.replace(")","")
                self.fDot.write(f' "{item}" ')
        self.fDot.write('}\n')

        self.fDot.write('subgraph outputs{rank="same"')
        for item in outputA:
            if item not in bufferA:
                if "(" in item:
                    item = item.replace("(","")
                if ")" in item:
                    item = item.replace(")","")
                self.fDot.write(f' "{item}" ')
        self.fDot.write('}\n')
    def setup2(self,rankDict): #function to prepare dot file
        #fDot.write('splines="ortho"\n')
        for key in rankDict:
            if key ==1:
                self.fDot.write('subgraph inputs{ rank="same"')
                for item in rankDict[key]:
                    self.fDot.write(f' "{item}" ')
                self.fDot.write('}\n')
            elif key == max(rankDict):
                self.fDot.write('subgraph outputs{rank="same"')
                for item in rankDict[key]:
                    self.fDot.write(f' "{item}" ')
                self.fDot.write('}\n')
            else:
                self.fDot.write(f'subgraph Rank{key}{{rank="same"')
                for item in rankDict[key]:
                    self.fDot.write(f' "{item[0]}" ')
                self.fDot.write('}\n')
    def writeNode(self,inN,shape):
        if shape == "circle":
            self.fDot.write(f'"{inN}" [shape={shape} fixedsize=true width = 0.7 height = 0.7]\n')
        else:
            self.fDot.write(f'"{inN}" [shape={shape}]\n')

    def writeEdgeNode(self,inN,outN="",label=""): 
        if label == "":
            self.fDot.write(f'"{inN}" -> "{outN}" \n')
        else:
            self.fDot.write(f'"{inN}" -> "{outN}" [label="{label}",fontcolor=red,fontweight=bolder]\n')
    def createSubgraph(self,input):
        self.fDot.write("subgraph{\nrand=same;")
        for item in input:
            self.fDot.write(f"{item};")
        self.fDot.write("\n}")
    def add_values_in_dict(sample_dict, key, list_of_values):
        ''' Append multiple values to a key in 
            the given dictionary '''
        if key not in sample_dict:
            sample_dict[key] = list()
        sample_dict[key].extend(list_of_values)
        return sample_dict
    def list_duplicates_of(seq,item):
        start_at = -1
        locs = []
        while True:
            try:
                loc = seq.index(item,start_at+1)
            except ValueError:
                break
            else:
                locs.append(loc)
                start_at = loc
        return locs
    def endFile(self):
        self.fDot.write("}")

class simulationInput:

    def and_gate(a, b):
        return str(int(a)&int(b))
    def not_gate(a):
        return str(int(not int(a)))
    def nor_gate(a, b):
        return str(int(not int(a) | int(b)))
    def xor_gate(a, b):
        return str(int(a) ^ int(b))
    def nand_gate(a, b):
        return str(int(not int(a)&int(b)))
    def or_gate(a, b):
        return str(int(a) | int(b))

    def rank(inputA,operationsA,bufferA,outputA):
        rankDict = {}
        inputRank = {}
        Rank = 1
        for item in inputA:
            if item not in bufferA and Rank not in inputRank:
                inputRank[Rank] = [item]
            elif item not in bufferA and item not in inputRank[Rank]:
                inputRank[Rank].append(item)
            elif item not in bufferA and item in inputRank[Rank]:
                # do nothing since the item is already in the list for the current rank
                pass
            else:
                pass
        savedRank = {}
        for key, value in inputRank.copy().items():
            print(key)
            for arrays in operationsA:
                if len(arrays[1]) >1:
                    if arrays[1][0] in value:
                        if arrays[1][0] in savedRank and savedRank[arrays[1][0]] > key+1:
                            pass
                        else:
                            savedRank[arrays[1][0]] = key
                            if key in rankDict:
                                rankDict[key].append(arrays)
                            else:
                                rankDict[key] = []
                                rankDict[key].append(arrays)
                            if key+1 in inputRank:
                                inputRank[key+1].append(arrays[2])
                            else:
                                inputRank[key+1] = []
                                inputRank[key+1].append(arrays[2])
                    if arrays[1][1] in value:
                        if arrays[1][1] in savedRank and savedRank[arrays[1][1]] > key+1:
                            pass
                        else:
                            savedRank[arrays[1][1]] = key
                            if key in rankDict:
                                rankDict[key].append(arrays)
                            else:
                                rankDict[key] = []
                                rankDict[key].append(arrays)
                            if key+1 in inputRank:
                                inputRank[key+1].append(arrays[2])
                            else:
                                inputRank[key+1] = []
                                inputRank[key+1].append(arrays[2])
                else:
                    if arrays[1][0] in value:
                        if arrays[1][0] in savedRank and savedRank[arrays[1][0]] > key+1:
                            pass
                        else:
                            savedRank[arrays[1][0]] = key
                            if key in rankDict:
                                rankDict[key].append(arrays)
                            else:
                                rankDict[key] = []
                                rankDict[key].append(arrays)
                            if key+1 in inputRank:
                                inputRank[key+1].append(arrays[2])
                            else:
                                inputRank[key+1] = []
                                inputRank[key+1].append(arrays[2])
        Rank = max(rankDict) +1
        for item in outputA:
            if item not in bufferA and Rank not in rankDict:
                rankDict[Rank] = [item]
            elif item not in bufferA and item not in rankDict[Rank]:
                rankDict[Rank].append(item)
            elif item not in bufferA and item in rankDict[Rank]:
                # do nothing since the item is already in the list for the current rank
                pass
            else:
                pass
        return rankDict




