class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_list = sorted([(p, s) for p, s in zip(position, speed)], key = lambda x: x[0])
        current_fleet_arrival_time = 0
        num_fleets = 0

        for p, s in sorted_list[::-1]:
            print(p,s)
            arrival_time = (target - p)/s
            if current_fleet_arrival_time < arrival_time:
                num_fleets += 1
                current_fleet_arrival_time = arrival_time
        
        return num_fleets
