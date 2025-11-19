class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in nums:
            cnt=0
            for j in nums:
                if i>j:
                    cnt+=1
            a.append(cnt)
        return a
                