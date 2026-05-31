class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(cars, key=lambda x: x[0])

        curr_fleet = len(cars) - 1
        fleets = 1

        for i in range(len(cars))[::-1]:
            if not (target - cars[i][0])/cars[i][1] <= (target - cars[curr_fleet][0])/cars[curr_fleet][1]:
                curr_fleet = i
                fleets += 1
        
        return fleets


             