infile = open("input6_2.txt", "r")
outfile= open("output6_2.txt", "w")

R, H = list(map(int, infile.readline().strip().split()))
grid = [list(infile.readline().strip()) for i in range(R)]

def dfs(grid, visited, r, c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or visited[r][c] or grid[r][c] == '#':
        return 0

    visited[r][c] = True
    d = 0

    if grid[r][c] == 'D':
        d += 1

    d += dfs(grid, visited, r + 1, c)
    d += dfs(grid, visited, r - 1, c)
    d += dfs(grid, visited, r, c + 1)
    d += dfs(grid, visited, r, c - 1)

    return d

max_d=0
visited = [[False] * H for i in range(R)]

def maximum(a,b):
    if a>b:
        return a
    else:
        return b

for i in range(R):
    for j in range(H):
        if grid[i][j] == '.':
            d = dfs(grid, visited, i, j)
            max_d = maximum(max_d, d)

infile.write(str(max_d))
infile.close()
outfile.close()