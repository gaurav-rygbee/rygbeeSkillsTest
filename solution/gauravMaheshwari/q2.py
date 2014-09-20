
#assuming case sensitive 

string1=raw_input("Please enter the first string -")	#the main input string
delimiters=raw_input("Please enter the delimiters-")	#string to be reversed
position=[]	#records all the occurance of the delimiters in string1
position.append(0)
delimit_list=list(delimiters)#converting it into a list 


for node in xrange(len(string1)):
	if string1[node] in delimit_list:
		position.append(node);  

position.append(len(string1))
#Now position contains all the position of delimiters but also the zero'th position delimiter


finalstring=[]

# i had to hardcode the first position and hence comparision to node = 0 because of the zero'th position delimiter

#get a substring between two delimiters and reverse it and then append the delimiter and then the reversed substring
for node in xrange(len(position)-1):
	if(node==0):
		if string1[0] in delimit_list:
			string=string1[position[node]+1: position[node+1]]
			stringReverse= string[::-1]
			finalstring.append(string1[position[node]])
			finalstring.append(stringReverse)
			#finalstring.append(string1[position[node]])
		else:
			string=string1[position[node]: position[node+1]]
			stringReverse= string[::-1]
			finalstring.append(stringReverse)
	else:	
		string=string1[position[node]+1: position[node+1]]#string between two delimiters
		stringReverse= string[::-1]#reversing the string
		finalstring.append(string1[position[node]])#appending the delimiter
		finalstring.append(stringReverse)#appending the reversed substring
		

print ''.join(finalstring)



