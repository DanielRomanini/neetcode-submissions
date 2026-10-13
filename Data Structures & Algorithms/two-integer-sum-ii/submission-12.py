class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while(r>l):
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1,1+r]
            if s<target:
                l+=1
            elif s>target:
                r-=1
        return 