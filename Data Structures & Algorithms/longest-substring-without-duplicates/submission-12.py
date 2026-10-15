class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        cur = 0
        most = 0
        l, r = 0,0
        while(r<len(s)):
            if s[r] not in hashmap: 
                hashmap[s[r]] = 1
            else:
                while(s[l] != s[r]):
                    hashmap.pop(s[l])
                    l+=1
                hashmap.pop(s[l])
                l+=1
                hashmap[s[r]] = 1
            most = max(most,len(hashmap))
            
            r+=1
        
        return most
