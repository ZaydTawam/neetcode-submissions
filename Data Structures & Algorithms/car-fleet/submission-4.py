class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_list = sorted([(p, s) for p, s in zip(position, speed)], key = lambda x: x[0])
        fleet_count = 0
        curr_fleet = 0

        for p, s in sorted_list[::-1]:
            time_to_target = (target - p)/s
            if time_to_target > curr_fleet:
                fleet_count += 1
                curr_fleet = time_to_target
        
        return fleet_count
