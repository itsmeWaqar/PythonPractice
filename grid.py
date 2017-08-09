def convertGridTo2D(grid):
	newGrid = {}
	for i in range(len(grid)):
		ls = list(grid[i])
		for j in range(len(ls)):
			if (i,j) not in newGrid:
				newGrid[(i,j)] = ls[j]
	return newGrid
def isValidSquare(grid, row, col):
	gr = grid[(row,col)]
	valid = grid.get((row,col), '-1')
	if valid == '0':
		return True
	return False


grid = ['0110', '0110', '0110', '0110' ]
new = convertGridTo2D(grid)

print isValidSquare(new, 0,0)
