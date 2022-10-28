from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        if m == 0:
            return None
        n = len(board[0])
        if n == 0:
            return None

        nextState = [[0 for x in range(n)] for y in range(m)]

        for i in range(m):
            for j in range(n):
                neighbours = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                alive_n = 0

                for point in neighbours:
                    if point[0] < 0 or point[0] >= m or point[1] < 0 or point[1] >= n:
                        continue

                    if board[point[0]][point[1]] > 0:
                        alive_n += 1

                if alive_n == 3 or (board[i][j] == 1 and alive_n == 2):
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

        for i in range(m):
            for j in range(n):
                board[i][j] = nextState[i][j]


s = Solution()
b = [[1,1],[1,0]]

s.gameOfLife(b)

print(b)