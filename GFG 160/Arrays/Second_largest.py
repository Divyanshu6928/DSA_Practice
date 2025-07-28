class Solution:
    def getSecondLargest(self, ar):
        # Code Here
        ans = -1
        second_max= ans
        
        for i in range(len(ar)):
            if(ar[i] > ans):
                ans = ar[i]
                
        for i in range(len(ar)):
            if(ar[i] != ans and ar[i] > second_max):
                second_max = ar[i]

        
        return second_max