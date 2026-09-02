class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        hashS = {}
        for c in s:
            if c not in hashS:
                hashS[c] = 1
            else:
                hashS[c] += 1
        
        hashT = {}
        for c in t:
            if c not in hashT:
                hashT[c] = 1
            else:
                hashT[c] += 1
        
        if (len(hashS) != len(hashT)):
            return False
        
        for char in hashS:
            if(char not in hashT):
                return False
            if(hashT[char] != hashS[char]):
                return False
        
        return True