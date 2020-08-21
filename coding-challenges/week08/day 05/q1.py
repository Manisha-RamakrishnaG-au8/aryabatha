class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        
        # In the case where there are i 2-steps. (0 <= i <= int(n/2)) 
        for two_step_count in range(int(n/2)+1):
            one_step_count = n - 2 * two_step_count
            total_step_count = one_step_count + two_step_count
            
            # Use a math formula for permutation with repetition
            combination = math.factorial(total_step_count) / (math.factorial(two_step_count)*math.factorial(one_step_count))
            result += int(combination)
        return result