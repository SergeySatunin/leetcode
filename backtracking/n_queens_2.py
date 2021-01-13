# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def __init__(self):
        self.n = 0
        self.under_attack = []
        self.queen_pos = []

    def totalNQueens(self, n: int) -> int:
        self.n = n
        return self.backtrack(0, 0)

    def backtrack(self, row=0, count=0):
        for col in range(self.n):
            # iterate through columns at the curent row.
            if self.is_not_under_attack(row, col):
                # explore this partial candidate solution, and mark the attacking zone
                self.place_queen(row, col)
                if row + 1 == self.n:
                    # we reach the bottom, i.e. we find a solution
                    count += 1
                else:
                    # we move on to the next row
                    count = self.backtrack(row + 1, count)
                # backtrack, i.e. remove the queen and remove the attacking zone.
                self.remove_queen(row, col)
        return count

    def is_not_under_attack(self, row, col):
        return (row,col) not in self.under_attack

    def get_attack_zone(self, row, col):
        attack = []
        attack.extend([(row, x) for x in range(self.n) if x != col])
        attack.extend([(x, col) for x in range(self.n) if x != row])

        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            attack.append((i, j))
            i -= 1
            j -= 1

        i = row + 1
        j = col + 1

        while i < self.n and j < self.n:
            attack.append((i, j))
            i += 1
            j += 1

        i = row - 1
        j = col + 1

        while i >= 0 and j < self.n:
            attack.append((i, j))
            i -= 1
            j += 1

        i = row + 1
        j = col - 1

        while i < self.n and j >= 0:
            attack.append((i, j))
            i += 1
            j -= 1

        return attack


    def place_queen(self, row, col):
        self.queen_pos.append((row,col))
        attack = self.get_attack_zone(row, col)
        self.under_attack.extend(attack)

    def remove_queen(self, row, col):
        self.queen_pos.remove((row, col))
        attack = self.get_attack_zone(row, col)
        for t in attack:
            self.under_attack.remove(t)
