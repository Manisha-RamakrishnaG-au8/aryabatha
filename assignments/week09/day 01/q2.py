class Solution:
    fib_list = []
    def fib(self, N: int) -> int:
        self.fib_list = [0, 1]
        if N < 2: return N
        for i in range(2, N+1):
            self.fib_list.append(self.fib_list[i-2] + self.fib_list[i-1])
        return self.fib_list[-1] 