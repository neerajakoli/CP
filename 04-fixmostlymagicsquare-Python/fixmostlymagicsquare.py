# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	p=[]
	for i in range(len(L)):
		p.extend(L[i])
	d=sorted(p)
	t=0
	for j in range(1,len(L)**2+1):
		if j in d:
			d.remove(j)
		else:
			t=j
	for i in range(len(L)):
		for j in range(len(L[0])):
			if(L[i][j]==d[0]):
				L[i][j]=t
	return L 

