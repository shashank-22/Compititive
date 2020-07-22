s1 = "asdf124eftvzqr001ebc144"

threedigitints = []

def findThreeGigitIntsFromString(s):
	count = 0
	tempnum = ""
	output = []
	for char in s1:
		if(char.isdigit()):
			count+=1
			tempnum+=char
		else:
			count=0
			tempnum = ""
		if(count==3):
			if(not tempnum.startswith("0")):
				output.append(int(tempnum))
	return output

print(findThreeGigitIntsFromString(s1))