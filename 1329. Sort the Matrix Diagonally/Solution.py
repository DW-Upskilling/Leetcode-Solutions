class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:

        # Iterates over first row
        for j in range(len(mat[0])):
            self.sort(mat, 0, j)
        # Iterates over first column
        for i in range(1, len(mat)):
            self.sort(mat, i, 0)
        
        return mat
    
    def sort(self, mat, x, y):

        values = []

        # Get all the values of the current diagonal matrix
        i = x
        j = y
        while i < len(mat) and j < len(mat[i]):
            values.append(mat[i][j])
            i += 1
            j += 1

        # using python inbuilt sort
        values.sort()

        # replacing sorted values back into the matrix
        i = x
        j = y
        while i < len(mat) and j < len(mat[i]):
            mat[i][j] = values[0]
            i += 1
            j += 1
            values.pop(0)