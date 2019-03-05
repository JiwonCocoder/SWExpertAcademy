inputString= input()
inputLength= len(inputString)
outputString= ""
for i in range(0,inputLength):
    tempChar=ord(inputString[i])
    if 65<=tempChar <=90 :
        tempChar= tempChar + 32
        #print(tempChar)
    outputString += chr(tempChar)
print(outputString)
	
    