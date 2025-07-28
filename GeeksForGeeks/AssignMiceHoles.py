#User function Template for python3

class Solution:
    def assignMiceHoles(self, N , M , H):
        # code here
        M.sort()
        H.sort()
        
        maxi = 0
        for i in range(N):
            if (maxi < abs(M[i] - H[i])):
                maxi = abs(M[i] - H[i])
                
        return maxi