class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Sliding window with varying lengths
        #Get the most of the same letters plus k different letters
        #store the most 
        most = 0
        l = 0
        hashtable = {}
        for r, char in enumerate(s):
            biggestHash = -1
            hashtable[char] = 1 + hashtable.get(char,0)
            length = r-l+1
            for char in hashtable:
                biggestHash = max(biggestHash,hashtable[char])
            while(length>biggestHash + k):
                hashtable[s[l]] -= 1
                l+=1
                length = r-l+1
            most = max(most,biggestHash+k)
        
        return min(len(s),most)
                