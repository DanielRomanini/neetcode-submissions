class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        print(s)
        while(r>l):
            if (not s[r].isalpha() and not s[r].isalnum()):
                r-=1
                continue
            if(not s[l].isalpha() and not s[l].isalnum()):
                l+=1
                continue
            print(s[l], s[r])
            if s[r] != s[l]:
                return False
            r-=1
            l+=1
        return True