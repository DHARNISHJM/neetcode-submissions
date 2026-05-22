class Solution:
    def binarySearch(self, arr: List[int], target: int):
        left = 0
        right = len(arr)-1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] < target:
                left = mid+1

            elif arr[mid] > target:
                right = mid-1
            
            else:
                return True
        return False




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1

        while left <= right:
            mid_row = (left + right) // 2
            res = self.binarySearch(matrix[mid_row], target)
            if res:
                return res
            else:
                if target > matrix[mid_row][0]:
                    left = mid_row + 1
                else:
                    right = mid_row - 1
        return False



        
