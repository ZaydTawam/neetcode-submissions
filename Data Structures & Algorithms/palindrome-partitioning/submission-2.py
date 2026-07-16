class Solution:
    def partition(self, s: str) -> List[List[str]]:
        vaild_branches = []

        def is_palindrome(start, end):
            l, r = start, end
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(branch, index):
            if index == len(s):
                vaild_branches.append(branch.copy())
            
            for i in range(index, len(s)):
                if not is_palindrome(index, i):
                    continue
                branch.append(s[index:i + 1])
                backtrack(branch, i + 1)
                branch.pop()
        
        backtrack([], 0)
        return vaild_branches