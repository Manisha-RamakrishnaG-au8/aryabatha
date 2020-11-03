class Solution(object):
    def isPalindrome(self, x):
        x = "".join(i for i in x if i.isalnum())
        return x.lower() == x[::-1].lower()