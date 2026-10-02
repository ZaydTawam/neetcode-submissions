class Solution:
    def partition(self, s: str) -> List[List[str]]:
        valid_splits = []
        seen = {}

        def is_palindrome(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True 

        def backtrack(index, split):
            if index == len(s):
                valid_splits.append(split.copy())
            
            for i in range(index, len(s)):
                substring = s[index:i + 1]
                if substring not in seen:
                    seen[substring] = is_palindrome(substring)
                if not seen[substring]:
                    continue
                
                split.append(substring)
                backtrack(i + 1, split)
                split.pop()
        
        backtrack(0, [])

        return valid_splits
# 0 
#   1 'a'
#       2 'a'
#           3 'b' 
#       3 'ab' x
#   2 'aa'
#       3 'b'
#   3 'aab' x