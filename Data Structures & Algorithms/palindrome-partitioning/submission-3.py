class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring):
            l, r = 0, len(substring) - 1
            while l <= r:
                if substring[l] != substring[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        def backtrack(index, substrings):
            print(index, substrings)
            if index == len(s):
                res.append(substrings.copy())
                return
            
            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                if not is_palindrome(substring):
                    continue
                substrings.append(substring)
                backtrack(i, substrings)
                substrings.pop()
        
        backtrack(0, [])
        return res

            