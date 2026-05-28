class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)%97] += 1
            if tuple(count) in counts:
                counts[tuple(count)].append(s)
            else:
                counts[tuple(count)] = [s]
        result = []
        for key in counts:
            result.append(counts[key])
        return result

        
        
        
        
        
        
        
        
        
        
        # freqs = {}
        # for s in strs:
        #     freq = {}
        #     for c in s:
        #         freq[c] = freq.get(c, 0) + 1
        #     freqs[s] = freq
        # print(freqs)
        # result = []
        # added = []
        # for s1 in freqs:
        #     if s1 in added:
        #         continue
        #     added.append(s1)
        #     group = [s1]
        #     for s2 in freqs:
        #         if s1 == s2: 
        #             continue
        #         if s2 in added:
        #             continue
        #         if freqs[s1] == freqs[s2]:
        #             added.append(s2)
        #             group.append(s2)
        #     result.append(group)

        # return result

