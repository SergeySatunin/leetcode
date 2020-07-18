# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        lena = len(a)
        lenb = len(b)

        if lena >= lenb:
            b = '0' * (lena - lenb) + b
            max_len = lena
        else:
            a = '0' * (lenb - lena) + a
            max_len = lenb

        move_flag = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            position = int(a[i]) + int(b[i])
            if position == 2:
                if move_flag == 1:
                    result.append(1)
                else:
                    result.append(0)
                move_flag = 1
            elif position == 1:
                result.append((position + move_flag) % 2)
            else:
                if move_flag == 1:
                    result.append(1)
                    move_flag = 0
                else:
                    result.append(0)

        if move_flag == 1:
            result.append(1)

        return ''.join([str(x) for x in reversed(result)])

s = Solution()
result = s.addBinary('10101','111101')

print(result)