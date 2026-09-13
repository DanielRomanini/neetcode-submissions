class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        s = s.lower()
        while(j>=i):
            while(j<len(s) and j>=0 and not s[j].isalnum()):
                j-=1
            while(i<len(s)-1 and not s[i].isalnum()):
                i+=1
            print(s[i], s[j])
            left = s[i]
            right = s[j]
            if left != right:
                return False
            i+=1
            j-=1
        
        return True