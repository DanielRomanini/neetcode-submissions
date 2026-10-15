class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashtableS1 = {}
        hashtableS2 = {}
        temp = "abcdefghijklmnopqrstuvwxyz"
        for char in temp:
            hashtableS1[char] = 0
            hashtableS2[char] = 0

        for char in s1:
            hashtableS1[char] += 1
        l = 0

        for r, char in enumerate(s2):
            length = r-l+1
            hashtableS2[char] += 1
            if length<len(s1):
                continue
            if length>len(s1):
                hashtableS2[s2[l]] -= 1
                l+=1
            if hashtableS2 == hashtableS1:
                return True
        
        return False