
class Solution:
    def totalElements(self, arr):
        left = 0
        n = len(arr)
        mydict = {}
        right = 0
        maxi = 0

        while right < n:
            mydict[arr[right]] = mydict.get(arr[right], 0) + 1
            if len(mydict) > 2:
                mydict[arr[left]] -= 1
                if mydict[arr[left]] == 0:
                    del mydict[arr[left]]
                left += 1
            if len(mydict) <= 2:
                maxi = max(maxi, right - left + 1)
            right += 1

        return maxi
    
s = Solution()

arr = [3, 1, 2,2 ,2 ,2]

print(s.totalElements(arr))
    