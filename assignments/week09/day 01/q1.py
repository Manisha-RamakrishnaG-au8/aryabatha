class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=amount)
        def consider(amount):
            if amount < 0: return -1
            if amount == 0: return 0
            mincount = sys.maxsize
            for coin in coins:
                cnt = consider(amount-coin)
                if 0 <= cnt < mincount:
                    mincount = cnt + 1
            res = mincount if mincount < sys.maxsize else -1
            return res
    
        return consider(amount)