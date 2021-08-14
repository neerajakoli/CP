# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.


import math
def fun_nearestbusstop(street):
	a=math.ceil(street/8)
	d=street-8*(a-1)
	b=8*(a)-street
	if(d==b):
		return 8*(a-1)
	c=min(b,d)
	if(min==d):
		return 8*(a-1)
	return 8*a
