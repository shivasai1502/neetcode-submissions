from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for ele in strs:
            so = "".join(sorted(ele))
            d[so].append(ele)
        
        return list(d.values())
            
        