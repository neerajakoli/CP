# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	if(n==0 and f!=0):
		return True # replace with your solution
	if(n==0 and f==0):
		return True 
	if(n!=0 and f==0):
		return False 
	return abs(n)%abs(f)==0