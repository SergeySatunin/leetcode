# https://leetcode.com/problems/sudoku-solver/

from collections import Counter
from typing import List
class Solution:

    def __init__(self):
        self.squares = {}
        self.squares[(1, 1)] = [range(0, 3), range(0, 3)]
        self.squares[(1, 4)] = [range(0, 3), range(3, 6)]
        self.squares[(1, 7)] = [range(0, 3), range(6, 9)]
        self.squares[(4, 1)] = [range(3, 6), range(0, 3)]
        self.squares[(4, 4)] = [range(3, 6), range(3, 6)]
        self.squares[(4, 7)] = [range(3, 6), range(6, 9)]
        self.squares[(7, 1)] = [range(6, 9), range(0, 3)]
        self.squares[(7, 4)] = [range(6, 9), range(3, 6)]
        self.squares[(7, 7)] = [range(6, 9), range(6, 9)]


    def isValidSolution(self, board):
        return len([board[i][j] for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == "."]) == 0

    def isValidCandidate(self, board, i, j, n):
        c = Counter(board[i])
        row_check = all([v <= 1 for (k,v) in c.items() if k != "."])
        c.clear()

        if not row_check:
            return False

        c = Counter([board[k][j] for k in range(len(board[0]))])
        column_check = all([v <= 1 for (k,v) in c.items() if k != "."])
        c.clear()

        if not column_check:
            return False

        min_dist = 100
        square_index = ()

        for t in self.squares.keys():
            d = abs(i - t[0]) + abs(j - t[1])
            if d < min_dist:
                min_dist = d
                square_index = t

        for k in range(-1,2):
            for n in range(-1,2):
                c[board[square_index[0] + k][square_index[1] + n]] += 1

        square_check = all([v <= 1 for (k,v) in c.items() if k != "."])

        return square_check

    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for n in range(1,10):
                        board[i][j] = str(n)
                        if self.isValidCandidate(board, i, j, n):
                            self.solveSudoku(board)

                            if self.isValidSolution(board):
                                return True

                        board[i][j] = "."
                    return False

        return True

s = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)

print(board)
