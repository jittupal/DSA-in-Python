class Solution:    
    def minPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        i = 1
        j = 0
        ans = 1
        count = 1
        n = len(arr)
        while i < n:
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans

S = Solution()
print(S.minPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))