class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        for n in nums:
            if not n in freqMap:
                freqMap[n] = 1
            else:
                freqMap[n] += 1
        for n in freqMap:
            if freqMap[n] > 1:
                return True
        return False