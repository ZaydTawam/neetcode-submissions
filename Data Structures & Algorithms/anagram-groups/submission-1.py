class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMaps = []
        output = []
        for s in strs:
            freqMap = {}
            for char in s:
                if char not in freqMap:
                    freqMap[char] = 1
                else:
                    freqMap[char] += 1
            if freqMap not in freqMaps:
                freqMaps.append(freqMap)
                output.append([s])
            else:
                i = freqMaps.index(freqMap)
                output[i].append(s)
        
        return output 
            
