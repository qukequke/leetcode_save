class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.res = ""

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i - 1:
                self.res = s[i + 1:j]

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res


print(Solution().longestPalindrome('aba'))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_len = 1
        n = len(s)
        start = 0
        for i in range(1, n):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            # print(even,odd)
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
            elif i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1

        return s[start: start + max_len]


print(Solution().longestPalindrome('ababbbaba'))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        """
        i = 0 j = 0, j = 1
        i = 1, j = 0 , j = 1, j = 2
        """
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i + 1 - j:
                    res = s[j: i + 1]
                    max_len = i + 1 - j
        for i in dp:
            print(i)
        return res
print(1)


print(Solution().longestPalindrome('ababbbaba'))
