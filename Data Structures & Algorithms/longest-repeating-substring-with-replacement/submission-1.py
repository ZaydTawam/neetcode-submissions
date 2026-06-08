class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, -1
        window = {}
        longest = 0
        while r < len(s) - 1:
            r += 1
            window[s[r]] = window.get(s[r], 0) + 1
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                if not window[s[l]]:
                    del window[s[l]]
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest

# 1 {"A": 1} 1
# 2 {"A": 2} 2
# 3 {"A": 3} 3
# 4 {"A": 3, "B": 1} 4
# 5 {"A": 4, "B": 1}