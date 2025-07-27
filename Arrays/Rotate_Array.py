class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        
        n = len(arr)
        rotate_dist = d % n
        temp = [0] * n
        
        for i in range(n-rotate_dist):
            temp[i] = arr[rotate_dist + i]
            
        for i in range(rotate_dist):
            temp[n-rotate_dist+i] = arr[i]
            
        for i in range(n):
            arr[i] = temp[i]
            
        return arr