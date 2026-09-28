class Solution:
            

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        string1Hash = {}
        string2Hash = {}
        for s in s1:
            if s not in string1Hash:
                string1Hash[s] = 1
            else:
                string1Hash[s] += 1

        for r in range(len(s2)):
            if s2[r] not in string2Hash:
                string2Hash[s2[r]] = 1
            else:
                string2Hash[s2[r]] += 1

            if (r-l+1 > len(s1)):
                if(string2Hash[s2[l]] == 1):
                    string2Hash.pop(s2[l])
                else:
                    string2Hash[s2[l]] -= 1
                l+=1
            print(string1Hash, string2Hash)
            if string1Hash == string2Hash:
                return True
        
        return False


    