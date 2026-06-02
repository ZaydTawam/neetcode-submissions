from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_required(k):
            num_hours = 0
            for pile in piles:
                num_hours += ceil(pile/k)
            return num_hours
        
        l, r = 1, max(piles)
        k = 0
        while l <= r:
            mid = (l + r)//2
            if hours_required(mid) > h:
                l = mid + 1
            else:
                k = mid
                r = mid - 1
        return k
