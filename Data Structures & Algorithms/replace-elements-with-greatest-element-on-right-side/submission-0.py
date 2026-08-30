class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArray = [0] * len(arr)
        newArray[-1] = -1
        currentMax = arr[-1]
        for i in range(len(arr) - 2, -1,-1):
            newArray[i] = currentMax
            if currentMax < arr[i]:
                currentMax = arr[i]
        print(newArray)
        return newArray