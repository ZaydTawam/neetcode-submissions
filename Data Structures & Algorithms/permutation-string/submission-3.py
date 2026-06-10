class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1)
        s1_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        window_count = {}

        for c in s2[l:r]:
            window_count[c] = window_count.get(c, 0) + 1

        while True:
            if s1_count == window_count:
                return True
            
            if r == len(s2):
                break

            window_count[s2[r]] = window_count.get(s2[r], 0) + 1
            window_count[s2[l]] -= 1
            if not window_count[s2[l]]:
                del window_count[s2[l]]
            
            l += 1
            r += 1

            


        return False
