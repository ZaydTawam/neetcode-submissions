from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            hours_taken = 0
            for pile in piles:
                hours_taken += ceil(pile/k)
            
            return hours_taken <= h

        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            if can_finish(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l