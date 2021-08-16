# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


from collections import Counter 
def mostfrequentdigit(n):
	a=str(n) 
	d=dict(Counter(a)) 
	s=d[max(d,key=d.get)] 
	l=[]
	for key, value in d.items():
		if(value==s):
			l.append(key)
	return int(min(l))

