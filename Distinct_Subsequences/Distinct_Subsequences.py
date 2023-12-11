class Solution(object):
    def numDistinct(self, s, t):
        n = len(s)
        m = len(t)

        dp = [0] * (m + 1)
        prev = [0] * (m + 1)

        dp[0] = 1 

        for i in range(1, n + 1):
            prev = dp[:]

            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = prev[j - 1] + prev[j]
                else:
                    dp[j] = prev[j]

        return dp[m]