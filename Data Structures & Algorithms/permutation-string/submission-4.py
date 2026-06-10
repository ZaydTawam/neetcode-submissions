class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        window_count = {}

        for c in s2[l:r]:
            window_count[c] = window_count.get(c, 0) + 1

        while r != len(s2):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            if s1_count == window_count:
                return True

            window_count[s2[l]] -= 1
            if not window_count[s2[l]]:
                del window_count[s2[l]]
            
            l += 1
            r += 1

            


        return False
