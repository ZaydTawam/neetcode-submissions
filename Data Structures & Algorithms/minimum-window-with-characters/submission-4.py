class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        count_window = {}
        l = 0
        for r in range(len(s)):
            if s[r] in count_t:
                count_window[s[r]] = count_window.get(s[r], 0) + 1
            
            while l <= r:
                valid = True
                for c in count_t:
                    if c not in count_window:
                        valid = False
                        break
                    elif count_window[c] < count_t[c]:
                        valid = False
                        break
                if not valid:
                    break
                if not shortest or len(shortest) > r - l + 1:
                    shortest = s[l:r + 1]
                if s[l] in count_window:
                    count_window[s[l]] -= 1

                    if not count_window[s[l]]:
                        del count_window[s[l]]
                
                l += 1
        
        return shortest
            

