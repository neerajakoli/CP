# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.
#     (12.0, 11), (14.2, 15),
    # (16.5, 17), (18.6, 19),
    # (25.0, 25), (27.2, 27),
    # (29.5, 29), (31.6, 31)

import math
def fun_nearestodd(n):
	s=str(n).split(".")
	print(s)
	if(int(s[0])%2!=0):
		return int(s[0])
	else:
		if(int(s[1])==0):
			return math.floor(n)-1
		return math.ceil(n)

