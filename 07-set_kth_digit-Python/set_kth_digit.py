# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 
# (468, 1, 3, 418)


def fun_set_kth_digit(n, k, d):
	c=abs(n)
	a=str(c)[::-1]
	if(k>len(a)-1):
		e=str(a)+str(d)
	else:
		e=str(a).replace(a[k],str(d))
	if(n<0):
		return int(e[::-1])*(-1)
	return int(e[::-1])

