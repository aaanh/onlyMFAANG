# https://leetcode.com/problems/reorganize-string/

class Solution:
    def max_except(self, table, last) -> int:
        res = -1
        largest = 0
        for i, el in enumerate(table):
            if el > largest and i != last:
                res = i
                largest = el
        return res
                
    def reorganizeString(self, s: str) -> str:
        start = ord('a')
        res = ""
        table = [0]*26
        for c in s:
            encode = ord(c) - start
            table[encode] += 1
        last = -1
        for _ in range(len(s)):
            most_index = self.max_except(table, last)
            if most_index == -1:
                return ""
            res += chr(most_index + start)
            table[most_index] -= 1
            last = most_index
        return res