def longestConsecutive(arr):
        n = len(arr)
        if n == 1:
            return 1
        max_count = 0
        for i in range(0, n):
            num = arr[i]
            count = 1
            while num+1 in arr:
                count += 1
                num += 1
            max_count = max(max_count, count)
        print(f"The Longest Sequence Is : {max_count}")
        #code here


arr = [1, 2,3, 78, 90, 4, 65, 2, 66, 67, 68, 69, 71, 72, 70]
longestConsecutive(arr)
