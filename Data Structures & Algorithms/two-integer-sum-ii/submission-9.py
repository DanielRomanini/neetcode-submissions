class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1

        while(r>l):
            twoSum = numbers[r] + numbers[l]
            if(twoSum == target):
                return [1+l,1+r];

            if(twoSum>target):
                r-=1
            else:
                l+=1
