class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = l = 0
        substring_set = set()
        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l += 1
            
            substring_set.add(s[r])

            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring