class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        
        def checkDiagonal(i, j, value):
            # print(i, j)
            while i < len(matrix) and j < len(matrix[i]):
                if matrix[i][j] != value:
                    # print(value, i, j)
                    return False
                i += 1
                j += 1
                
            return True
        
        for i in range(len(matrix)-1):
            if not checkDiagonal(i, 0, matrix[i][0]):
                return False
        
        for i in range(1, len(matrix[0])-1):
            if not checkDiagonal(0, i, matrix[0][i]):
                return False
            
        return True
            