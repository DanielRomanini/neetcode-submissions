class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Have a window of length 3 go across the entire array
        #Sort the window
        #check if its equals to sorted s1

        string1 = []
        for char in s1:
            string1.append(char)
        string1.sort()

        lengthS1 = len(s1)
        l = 0
        temp = []
        for r in range(len(s2)):
            temp.append(s2[r])
            length = r-l+1
            if length<lengthS1:
                continue
            if length>lengthS1:
                temp.remove(s2[l])
                l+=1
            temp2 = temp
            temp2.sort()
            if(temp2 == string1):
                return True
        return False
            
