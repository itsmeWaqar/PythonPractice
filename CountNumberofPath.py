
def count_the_paths(grid):
	global paths
	paths = {}
	global MaxCol
	MaxCol = len(grid[0]) #Max coloumn length
	convGrid = convertGridTo2D(grid)
	row = len(grid) -1
	col = 0
	no = count_paths(convGrid, row , col)
	return no % 1000003

def count_paths(grid, row, col):
	#base case
	if not isValidSquare(grid, row, col):
		return 0
	elif isAtEnd(grid, row, col):
		return 1
	else:
		if (row,col) not in paths:
			paths[row, col] = count_paths(grid, row-1, col) + count_paths(grid, row, col-1)
		return paths[row,col]

def isValidSquare(grid, row, col):
	valid = grid.get((row,col), '-1')
	if valid == '0':
		return True
	else:
		return False

def isAtEnd(grid, row, col):
	if row == 0 and col == MaxCol-1:
		return True
	else:
		return False

def convertGridTo2D(grid):
	newGrid = {}
	for i in range(len(grid)):
		ls = list(grid[i])
		for j in range(len(ls)):
			if (i,j) not in newGrid:
				newGrid[(i,j)] = ls[j]
	return newGrid


gridd = ['0110', '0110', '0110', '0110' ]
num = count_the_paths(gridd)
print num