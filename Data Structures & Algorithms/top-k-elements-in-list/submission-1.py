class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies
        d = {}
        for ele in nums:
            if ele not in d:
                d[ele] = 1
            else:
                d[ele] += 1
        
        sorted_elements = sorted(d.items(), key=lambda item: item[1], reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(sorted_elements[i][0])
            
        return ans