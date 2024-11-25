#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self, arr):
        max_so_far = arr[0]
        min_so_far = arr[0]
        result = arr[0]
        for i in range(1, len(arr)):
            num = arr[i]
            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)
            result = max(result, max_so_far)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
