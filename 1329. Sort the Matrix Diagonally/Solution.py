class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:

        # print(mat)

        for j in range(len(mat[0])):
            # print(j)
            self.sort(mat, 0, j)
        # print(len(mat))
        for i in range(1, len(mat)):
            # print(i)
            self.sort(mat, i, 0)
        
        # print(mat)
        
        return mat
    
    def sort(self, mat, x, y):

        # print(x, y)
        values = []

        i = x
        j = y
        while i < len(mat) and j < len(mat[i]):
            values.append(mat[i][j])
            i += 1
            j += 1

        # print(values)

        values.sort()

        i = x
        j = y
        while i < len(mat) and j < len(mat[i]):
            mat[i][j] = values[0]
            i += 1
            j += 1
            values.pop(0)