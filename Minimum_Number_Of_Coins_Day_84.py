class Solution:
    def findMin(self, n):
        ans = 0
        ans += (n // 10)
        n = n % 10
        ans += (n // 5)
        n = n % 5
        ans += (n // 2)
        n = n % 2
        ans += (n // 1)
        print(ans)


S = Solution()
S.findMin(29)
S.findMin(45)