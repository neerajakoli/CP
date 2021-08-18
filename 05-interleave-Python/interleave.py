# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	s=""
	for i in range(min(len(s1),len(s2))):
		s+=s1[i]
		s+=s2[i]
	a=len(s1)
	b=len(s2)
	c=max(a,b)
	if(c==a):
		s+=s1[min(len(s1),len(s2)):]
	else:
		s+=s2[min(len(s1),len(s2)):]
	return s 
