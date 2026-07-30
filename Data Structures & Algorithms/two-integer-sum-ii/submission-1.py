class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        ans=[]
        s=numbers
        while l<r:
            if l<r and s[l]+s[r]<target:
                l+=1
            elif l<r and s[l]+s[r]>target:
                r-=1
            else:
                return [l+1,r+1]
        
