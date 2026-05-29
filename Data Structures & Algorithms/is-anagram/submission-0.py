class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}

        n = len(s)
        m = len(t)

        if n!=m:
            return False
        
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            
            if t[i] not in d:
                d[t[i]] = -1
            else:
                d[t[i]] -= 1
        
        for ele in d:
            if d[ele]!=0:
                return False
        return True
        