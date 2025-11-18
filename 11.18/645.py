class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        S = sum(nums)                    
        T = n * (n + 1) // 2             
        seen = set()
        for v in nums:                   
            if v in seen:
                dup = v                  
                break
            seen.add(v)
        missing = dup - (S - T)         
        return [dup, missing]