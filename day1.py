#  DAY 1 OF GFG : PROGRAM TO FIND THE 2ND LARGEST NUMBER IN AN ARRAY

class Solution:
    def getSecondLargest(self, arr):
        largest = second_largest = float('-inf')
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        
        return second_largest if second_largest != float('-inf') else -1

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        arr = list(map(int, input("Enter array elements: ").split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")