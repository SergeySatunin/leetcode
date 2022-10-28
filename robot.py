class Solution():
    def __init__(self, area):
        self.area = area
        self.rows = len(area) - 1
        if self.rows >= 0:
            self.cols = len(area[0]) - 1

        self.attempted = {}

    def solution(self, current_pos, current_dir):
        if not current_pos:
            current_pos = (0, 0)

        current_key = str(current_pos[0]) + str(current_pos[1])

        if current_key not in self.attempted:
            self.attempted[current_key] = []

        if self.rows == 0 and self.cols == 0:
            return

        if current_key in self.attempted and current_dir in self.attempted[current_key]:
            return

        if current_dir == "right":
            if current_pos[1] < self.cols and self.area[current_pos[0]][current_pos[1] + 1] != 'X':
                self.attempted[current_key].append("right")
                self.solution((current_pos[0], current_pos[1] + 1), "right")
            else:
                self.solution((current_pos[0], current_pos[1]), "down")
        elif current_dir == "down":
            if current_pos[0] < self.rows and self.area[current_pos[0] + 1][current_pos[1]] != 'X':
                self.attempted[current_key].append("down")
                self.solution((current_pos[0] + 1, current_pos[1]), "down")
            else:
                self.solution((current_pos[0], current_pos[1]), "left")
        elif current_dir == "left":
            if current_pos[1] - 1 >= 0 and self.area[current_pos[0]][current_pos[1] - 1] != 'X':
                self.attempted[current_key].append("left")
                self.solution((current_pos[0], current_pos[1] - 1), "left")
            else:
                self.solution((current_pos[0], current_pos[1]), "up")
        else:
            if current_pos[0] - 1 >= 0 and self.area[current_pos[0] - 1][current_pos[1]] != 'X':
                self.attempted[current_key].append("up")
                self.solution((current_pos[0] - 1, current_pos[1]), "up")
            else:
                self.solution((current_pos[0], current_pos[1]), "right")


#area = ["....X..", "X......", ".....X.", "......."]
#area = ["...X..", "....XX", "..X..."]
area = ["..", ".X"]

s = Solution(area)
s.solution((0,0), "right")

print(len(s.attempted))