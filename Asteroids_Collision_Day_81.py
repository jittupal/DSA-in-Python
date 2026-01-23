class Solution:
    def asteroidCollision(self, asteroids):
        st = []
        n = len(asteroids)
        for i in range(0, n):
            if asteroids[i] > 0:
                st.append(asteroids[i])
            else:
                while len(st) != 0 and st[-1] > 0 and st[-1] < abs(asteroids[i]):
                    st.pop()
                if len(st) != 0 and st[-1] == abs(asteroids[i]):
                    st.pop()
                elif len(st) == 0 or st[-1] < 0:
                    st.append(asteroids[i])
        return st
    
arr = [2, 3, 5, 3, -4, 6]

s = Solution()

ans = s.asteroidCollision(arr)

print(ans)
