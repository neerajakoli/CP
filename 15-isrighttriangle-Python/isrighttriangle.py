# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	a=math.sqrt((x1-x2)**2+(y1-y2)**2)
	b=math.sqrt((x1-x3)**2+(y1-y3)**2)
	c=math.sqrt((x3-x2)**2+(y3-y2)**2)
	d=max(a,b,c)
	e=min(a,b,c)
	f=a+b+c-d-e
	if(round(d**2)==round(e**2+f**2)):
		return True 
	return False 

