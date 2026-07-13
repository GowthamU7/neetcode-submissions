class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*27
        if len(s) != len(t):
            return False
        
        for i in s:
            count[ord(i)-96]+=1

        for j in t:
            count[ord(j)-96]-=1
        for i in count:
            if i != 0:
                return False
        return True
            