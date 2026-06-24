class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_count = {}
        l, r = 0, -1
        longest = 0
        while r < len(s) - 1:
            r += 1
            window_count[s[r]] = window_count.get(s[r], 0) + 1
            while r - l + 1 - max(window_count.values()) > k:
                window_count[s[l]] -= 1
                if not window_count[s[l]]:
                    del window_count[s[l]]
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest