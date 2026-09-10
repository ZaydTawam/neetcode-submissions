class Solution:
    def partition(self, s: str) -> List[List[str]]:
        checked_substrings = {}
        def is_palindrome(substring):
            l, r = 0, len(substring) - 1
            while l < r:
                if substring[l] != substring[r]:
                    checked_substrings[substring] = False
                    return
                l += 1
                r -= 1
            checked_substrings[substring] = True

        res = []
        def backtrack(index, substrings):
            print(index, substrings)
            if index == len(s):
                res.append(substrings.copy())
                return
            
            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                if substring not in checked_substrings:
                    is_palindrome(substring)
                if not checked_substrings[substring]:
                    continue 
                substrings.append(substring)
                backtrack(i, substrings)
                substrings.pop()
        
        backtrack(0, [])
        return res

            