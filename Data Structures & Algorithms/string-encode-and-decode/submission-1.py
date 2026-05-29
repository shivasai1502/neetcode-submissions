class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for ele in strs:
            res=res+str(len(ele))+"#"+ele
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        n = len(s)

        i = 0

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            st = s[j+1 : j+1+length]
            res.append(st)
            i = j + 1 + length
        return res
