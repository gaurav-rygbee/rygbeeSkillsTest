#Given two strings, reverse all the occurrences of second string in the first string.
#    Input: Two strings
#   Output: First string with every occurrence of second string reversed.



string1=raw_input("Please enter the first string -")	#the main input string
string2=raw_input("Please enter the string to be reversed -")	#string to be reversed
stringReverse= string2[::-1]	#extended slicing operation for reversing the given string stored in string2
string1Reversed=string1.replace(string2,stringReverse)	#reversed string1 stored in string1Reversed
print string1Reversed 