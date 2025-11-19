class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        m=max(nums)
        n=len(nums)
        while original<=m:
            if original in nums:
                original=original*2
            else:
                break
        return original