class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0

        longest = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

            while r-l+1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                if not counts[s[l]]:
                    del counts[s[l]]
                l += 1
            
            longest = max(r-l+1, longest)

        return longest

# AAABABB
# ^
#  ^