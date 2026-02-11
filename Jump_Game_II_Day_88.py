class Solution:
    def jump(self, nums):
        left = 0
        right = 0
        jump = 0
        n = len(nums)
        farthest = 0
        while right < n - 1:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jump += 1
        return jump

S = Solution()
ans = S.jump([2,2,1,1,4])
print(ans)