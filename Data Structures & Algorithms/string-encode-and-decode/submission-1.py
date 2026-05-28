class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s + "-"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        last = 0
        for i in range(len(s)):
            if s[i] == "-":
                result.append(s[last:i])
                last = i + 1
        
        return result