# https://leetcode.com/problems/largest-time-for-given-digits/

from typing import List
import copy

class Solution:

    def __init__(self):
        self.permutations = []

    def largestTimeFromDigits(self, arr: List[int]) -> str:

        hour_candidates = []
        minute_candidates = []

        for pos1, i in enumerate(arr):
            for pos2, j in enumerate(arr):
                if pos1 != pos2:
                    cand = int(str(i) + str(j))
                    if cand >= 0 and cand <= 23:
                        hour_candidates.append(cand)

        for hours in sorted(hour_candidates, reverse=True):

            tmp_arr = copy.deepcopy(arr)
            if hours < 10:
                drop1 = 0
                drop2 = hours
            else:
                drop1 = int(str(hours)[0])
                drop2 = int(str(hours)[1])

            tmp_arr.remove(drop1)
            tmp_arr.remove(drop2)

            for pos1, i in enumerate(tmp_arr):
                for pos2, j in enumerate(tmp_arr):
                    if pos1 != pos2:
                        cand = int(str(i) + str(j))
                        if cand >= 0 and cand <= 59:
                            minute_candidates.append(cand)

            if len(minute_candidates) == 0:
                continue
            else:
                mi = max(minute_candidates)
                return (str(hours) if len(str(hours)) == 2 else '0' + str(hours)) + ':' + ('0' + str(mi) if len(str(mi)) == 1 else str(mi))

        return ""