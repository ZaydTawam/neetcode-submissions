class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        for n in nums:
            if not n in freqMap:
                freqMap[n] = 1
            else:
                return True
        return False