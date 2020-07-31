class Solution:
    def addStrings(self, str(num1),str(num2)) -> str:
        sum = ""
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0:
            carry += ord(num1[i]) - 48 if i >= 0 else 0
            carry += ord(num2[j]) - 48 if j >= 0 else 0

            sum += str(carry % 10)
            carry //= 10