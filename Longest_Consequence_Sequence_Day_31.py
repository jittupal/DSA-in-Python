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

def longestConsecutive1(arr):
        my_set = set()
        n = len(arr)
        for i in range(0, n):
            my_set.add(arr[i])
        
        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                
                longest = max(longest, count)
                
        print(f"The Longest Sequence Is : {longest}")

arr = [1, 2,3, 78, 90, 4, 65, 2, 66, 67, 68, 69, 71, 72, 70]
longestConsecutive(arr)
longestConsecutive1(arr)