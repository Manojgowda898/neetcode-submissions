class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        queue = deque()

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 0:
                    queue.append( (row, col) )

        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 2147483647):

                        grid[nr][nc] = grid[r][c] + 1
                        queue.append( (nr, nc))



        