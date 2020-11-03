class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystring = s.lower()
        mystring2 = ""
        for i in mystring:
            if i.isalnum():
                mystring2 += i
        return mystring2
    
        for i in range(0, int(len(mystring2)/2)):  
            if mystring2[i] != mystring2[len(mystring2)-i-1]: 
                return False
        return True