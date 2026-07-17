class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_characters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        combinations = []

        def backtrack(combination):
            if len(combination) == len(digits):
                combinations.append(''.join(combination))
                return
            
            for c in digit_characters[digits[len(combination)]]:
                combination.append(c)
                backtrack(combination)
                combination.pop()

        backtrack([])
        return combinations