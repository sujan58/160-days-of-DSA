#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        i = n - 2

        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]

        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
