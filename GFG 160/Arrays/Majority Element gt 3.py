class Solution:
    def findMajority(self, arr):
        # code here
        hm = {}
        n = len(arr)
        for i in range(n):
            # c = 0
            if arr[i] in hm:
                hm[arr[i]] += 1
            else:
                hm[arr[i]] = 1
                
        pause = n//3
        res = []
        
        for key in hm:
            if hm[key] > pause:
                res.append(key)
                
        return sorted(res)