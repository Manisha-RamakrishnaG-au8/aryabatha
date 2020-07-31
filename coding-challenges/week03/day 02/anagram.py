class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        s_count = [0] * 26
        t_count = [0] * 26
        for elem in s:
            s_count[ord(elem)-97] += 1
        for elem in t:
            t_count[ord(elem)-97] += 1
        return s_count == t_count