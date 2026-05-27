class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        #trick is to treat it as one big matrix

        left = 0
        right = r*c - 1

        while(left <= right):
            midpoint = (left + right) // 2

            #convert into matrix indices
            indexR = midpoint // c
            indexC = midpoint % c

            if matrix[indexR][indexC] < target:
                left = midpoint + 1
            
            elif matrix[indexR][indexC] > target:
                right = midpoint - 1
            else:
                return True
        
        return False


        