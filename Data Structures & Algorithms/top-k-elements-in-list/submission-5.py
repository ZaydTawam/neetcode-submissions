class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        res = []
        for i in range(k):
            most_freq = [-1001, 0]
            for key in counts:
                if counts[key] > most_freq[1]:
                    most_freq = [key, counts[key]]
            del counts[most_freq[0]]
            res.append(most_freq[0])
        
        return res

