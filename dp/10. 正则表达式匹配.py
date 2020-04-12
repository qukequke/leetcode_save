class Solution:
    def firstmatch(self, s, p, i, j):
        return s[i] == p[j] or p[j] == '.'

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(p)):  # 初始化 s为空的时候 p有时候可以为True 例如a*  后面迭代会用到
            if p[i] == '*':
                dp[0][i + 1] = dp[0][i - 1]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':  # 判断dp[i][j]的时候 要看p[j-1]的状态 如果是* 考虑的比较多，不是*比较简单
                    # 两种情况  一种是pattern直接向后退2个 不要  '任意字符*' 了 另一种是 匹配当前字符 字符向前退一个
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and self.firstmatch(s, p, i - 1, j - 2))
                else:  # p[j-1]不是* 可以直接匹配当前字母 以及 之前状态
                    print(i, j)
                    dp[i][j] = dp[i - 1][j - 1] and self.firstmatch(s, p, i - 1, j - 1)
        for i in dp:
            print(i)
        return dp[-1][-1]


s = "aab"
p = "c*a*b"
ret = Solution().isMatch(s, p)
print(ret)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)

        dp = [[False] * (np + 1) for _ in range(ns + 1)]
        dp[0][0] = True
        # 匹配空字符串的情况, 匹配串为空时已经为False, 不再更新
        for i in range(np):
            # 根据规则, *前必存在一个字符, 则当前为*时, 其状态与前2的状态一致
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True
        # 更新状态矩阵
        # print(dp)
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                # i,j是矩阵的行与列, 对应到匹配串和字符串的索引要-1
                # 匹配串与字符串匹配(相等或为.)传递状态
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # 匹配串中 * 字符特殊处理
                elif p[j - 1] == '*':
                    # 根据匹配规则, 比较匹配串*的前一个字符与字符串中前一个字符
                    # 二者不相等时, a*只有作为空字符串时才可能匹配,
                    # 这就是说, 略过前一个字符, *字符对应的状态与字符串中前2个字符的状态一致
                    if p[j - 2] != s[i - 1]:
                        dp[i][j] = dp[i][j - 2]
                    # 二者相等时有三种情况
                    # a*作为: 空字符, 单字符 a, 多字符 aaa...
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]
        for i in dp:
            print(i)
        return dp[ns][np]


ret = Solution().isMatch(s, p)
# print(ret)
