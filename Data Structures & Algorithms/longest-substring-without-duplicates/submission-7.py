class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        most = 0
        queue = deque()
        hashtable = {}
        for r in range(len(s)):
            queue.append(s[r])
            if s[r] not in hashtable:
                hashtable[s[r]] = 1
            else:
                hashtable[s[r]] += 1
            
            while(len(queue)>0 and hashtable[s[r]] > 1):
                hashtable[s[l]] -= 1
                queue.popleft()
                l+=1
            
            most = max(most,r-l+1)
            
        return most
            