# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, input: str) -> bool:

        stack = []

        for i in input:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                l = len(stack)
                if l == 0:
                    stack.append(i)
                    break

                if i == ')':
                    if stack[len(stack) - 1] == '(':
                        stack.pop()
                    else:
                        break
                elif i == ']':
                    if stack[len(stack) - 1] == '[':
                        stack.pop()
                    else:
                        break
                else:
                    if stack[len(stack) - 1] == '{':
                        stack.pop()
                    else:
                        break

        return len(stack) == 0


input = "([)]"
s = Solution()
result = s.isValid(input)

print(result)