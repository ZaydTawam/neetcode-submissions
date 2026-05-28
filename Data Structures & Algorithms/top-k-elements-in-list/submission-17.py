class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        counts = [[] for _ in range(len(nums) + 1)]
        for key, val in freq_map.items():

            counts[val].append(key)
        res = []
        for arr in counts[::-1]:
            if not arr:
                continue
            for num in arr:
                res.append(num)
                if len(res) == k:
                    return res

        
        
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        # res = []
        # for i in range(k):
        #     most_freq = [0, 0]
        #     for key in counts:
        #         if counts[key] > most_freq[1]:
        #             most_freq = [key, counts[key]]
        #     del counts[most_freq[0]]
        #     res.append(most_freq[0])
        
        # return res

