class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        window = set()

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        for r in range(len(s)):
            while(s[r] in window):
                window.remove(s[l])
                l+=1
            length = max(length,r-l+1)
            window.add(s[r])
            
        return length

