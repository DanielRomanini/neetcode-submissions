class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashtable = {}
        l = 0
        length = 0
        frequent = -1
        if len(s)==0:
            return 0

        for r in range(len(s)):
            if s[r] not in hashtable:
                hashtable[s[r]] = 1
            else:
                hashtable[s[r]] += 1
            for num in hashtable:
                if frequent<hashtable[num]:
                    frequent = hashtable[num]
            while(r-l+1-frequent>k):
                hashtable[s[l]] -= 1
                l+=1
            length = max(length,r-l+1)
        
        return length