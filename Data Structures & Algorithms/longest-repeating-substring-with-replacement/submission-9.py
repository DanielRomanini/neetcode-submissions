class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashtable = {}
        most = 0
        l = 0
        for r,char in enumerate(s):
            hashtable[char] = hashtable.get(char,0) + 1
            biggestHash = 0
            for char in hashtable:
                biggestHash = max(biggestHash,hashtable[char])
            length = r-l+1
            if(length<=biggestHash+k):
                most = max(most,length)
            while(length>biggestHash+k):
                hashtable[s[l]] -= 1
                l+=1 
                length = r-l+1

        return most           
        