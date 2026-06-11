class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        shortest_substring = ""
        l, r = 0, len(t) - 1

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        count_window = {}
        for c in s[:len(t)]:
            if c in count_t:
                count_window[c] = count_window.get(c, 0) + 1

        print(count_t)
        while True:
            print(count_window, l, r)
            
            match = True
            for key, value in count_t.items():
                if count_window.get(key, 0) < value:
                    match = False
                    break

            if match:
                if not shortest_substring or (r - l + 1) < len(shortest_substring):
                    shortest_substring = s[l:r+1]
                
                if s[l] in count_t:
                    count_window[s[l]] -= 1
                    if not count_window[s[l]]:
                        del count_window[s[l]]
                l += 1
            else:
                if r >= len(s) - 1:
                    break
                r += 1
                if s[r] in count_t:
                    count_window[s[r]] = count_window.get(s[r], 0) + 1
        
        return shortest_substring

        


# "OUZODYXAZV"
#  ^ ^

# if window not valid:
#   increase r

# if window valid
#   if len window < len shortest
#       save len
#   increase l