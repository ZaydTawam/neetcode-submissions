class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, -1
        window = set()
        longest = 0
        while r < len(s) - 1:
            r += 1
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])

            longest = max(len(window), longest)
        
        return longest
