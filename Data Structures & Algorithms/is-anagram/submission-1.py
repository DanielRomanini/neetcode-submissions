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

        return hashS == hashT