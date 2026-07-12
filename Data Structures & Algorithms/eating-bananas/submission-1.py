from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
            
            return h >= hours
        
        left, right = 1, max(piles)
        min_k = 0
        while left <= right:
            mid = (left + right)//2
            if can_finish(mid):
                right = mid - 1
                min_k = mid
            else:
                left = mid + 1

        return min_k