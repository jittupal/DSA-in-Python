class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(0, len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i+nums[i])
        return True
    
S = Solution()
print(S.canJump([1,2,3,0,4]))