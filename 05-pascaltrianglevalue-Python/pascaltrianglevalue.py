# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	if(col>row):
		return 0 
	rows = [[1], [1, 1]]
	if(row>2):
		for i in range(2,row):
			r = [1]
			for j in range(1,i):
				r.append(rows[-1][j] + rows[-1][j - 1])
			r.append(1)
		rows.append(r)
	print(rows)
	return rows[row][col]

print(fun_pascaltrianglevalue(5,2))  
