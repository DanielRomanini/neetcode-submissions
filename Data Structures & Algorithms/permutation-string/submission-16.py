class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = "abcdefghijklmnopqrstuvwxyz"
        hashmap1 = {}
        hashmap2 = {}
        for c in temp:
            hashmap1[c] = 0
            hashmap2[c] = 0
        for c in s1:
            hashmap2[c] += 1
        
        l = 0
        for r, char in enumerate(s2):
            print(hashmap1, char)
            hashmap1[char] += 1
            if(r-l+1>len(s1)):
                hashmap1[s2[l]] -= 1
                l+=1
            if(hashmap1 == hashmap2):
                return True
        return False