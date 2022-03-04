# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if len(stack) > 0 and stack[-1][0] == '(' and char == ")":
                stack.pop()
            elif char == '(' or char == ")":
                stack.append((char,i))
        s = list(s)
        for el in stack:
            s[el[1]] = ""
        return "".join(s)