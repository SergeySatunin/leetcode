# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        end_times = []
        max_depth = 0

        for i, interval in enumerate(sorted_intervals):
            l_end_times = len(end_times)

            if l_end_times == 0:
                end_times.append(interval[1])
                continue

            min_end_times = min(end_times)

            if interval[0] >= min_end_times:
                max_depth = max(max_depth, l_end_times)
                end_times.remove(min_end_times)
                end_times.append(interval[1])
            else:
                end_times.append(interval[1])

        return max(max_depth, len(end_times))

s = Solution()
res = s.minMeetingRooms( [[7,10],[2,4]])

print(res)