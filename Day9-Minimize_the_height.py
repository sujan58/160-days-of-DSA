class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        res = arr[n-1] - arr[0]
        for i in range(1,len(arr)):
            if arr[i]-k< 0:
                continue
            
            minH=min(arr[0]+k,arr[i]-k)
            maxH=max(arr[i-1]+k,arr[n-1]-k);
            res=min(res,maxH-minH)
        
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
