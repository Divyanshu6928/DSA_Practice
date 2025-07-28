class Solution:
    def pushZerosToEnd(self,ar):
        # code here
        n= len(ar)
        i = 0 
        for j in range(n):
            if (ar[j] != 0):
                ar[i] , ar[j] = ar[j] , ar[i]
                i+=1
                
        return ar