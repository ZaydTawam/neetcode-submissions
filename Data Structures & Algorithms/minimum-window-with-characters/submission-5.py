class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = None

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        need = len(count_t)
        have = 0

        count_window = {}
        l = 0
        for r in range(len(s)):
            if s[r] in count_t:
                count_window[s[r]] = count_window.get(s[r], 0) + 1
            
                if count_window[s[r]] == count_t[s[r]]:
                    have += 1

            while have == need:
                if not shortest or shortest[1] - shortest[0] + 1 > r - l + 1:
                    shortest = (l, r)
                
                if s[l] in count_window:
                    if count_window[s[l]] == count_t[s[l]]:
                        have -= 1
                    count_window[s[l]] -= 1

                    if not count_window[s[l]]:
                        del count_window[s[l]]
                
                l += 1
        
        return s[shortest[0]:shortest[1] + 1] if shortest else ""
            

