#author tom mulvey
# date 10/31/17
# purpose : cost grid. given a grid, find shorted path

grid = ([3,8,1],[2,7,2], [4,4,3]) #can change the grid.

def rec_shortest(grid, y, x) :
	if y < 0 or x < 0:
		return float("inf")
	elif y == 0 and x == 0 :
		return grid[0][0]
	else :
		return grid[y][x] + min(rec_shortest(grid, y-1,x-1), \
					rec_shortest(grid, y-1, x), \
					rec_shortest(grid, y, x-1))

print(rec_shortest(grid, 1,2))
