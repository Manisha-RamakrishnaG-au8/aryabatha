import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = n-1
        d = m-1
        ans = math.factorial(r+d) /(math.factorial(r) * math.factorial(d))
        return int(ans)