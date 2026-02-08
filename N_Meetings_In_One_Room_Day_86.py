#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        meetings = list(zip(start, end))
        meetings.sort(key=lambda x:x[1])
        count = 1
        lastend = meetings[0][1]
        for i in range(1, len(meetings)):
            if meetings[i][0] > lastend:
                count += 1
                lastend = meetings[i][1]
        return count
    
S = Solution()
ans = S.maximumMeetings([0,1,2,3,4], [2,4,6,7,9])
print(ans)