class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        print(matrix, k)
        maxSum = float('-inf')

        m = len(matrix)
        n = len(matrix[0])
        # make prefix sum for each row
        for r in range(m):
            if maxSum < matrix[r][0] and matrix[r][0] <= k:
                maxSum = matrix[r][0]
            for c in range(1, n):
                if maxSum < matrix[r][c] and matrix[r][c] <= k:
                    maxSum = matrix[r][c]
                matrix[r][c] += matrix[r][c-1]
                if maxSum < matrix[r][c] and matrix[r][c] <= k:
                    maxSum = matrix[r][c]
        if maxSum == k: return maxSum

        print(matrix, maxSum)
        print(m, 'x', n)
        for r in range(2, m+1):
            for rs in range(0, m-(r-1)):
                for c in range(n):
                    for cs in range(n):
                        # print(rs, r, cs, c)
                        s = 0
                        for i in range(rs, r+rs):
                            if cs == 0:
                                s += matrix[i][c]
                                print(rs, i, cs, matrix[i][c], s)
                            else:
                                s += matrix[i][c] - matrix[i][cs-1]
                                print(r, rs, i, c, cs-1, matrix[i][c], matrix[i][cs-1], "--", s)
                        print(s)
                        if s > maxSum and s <= k:
                            maxSum = s
                        if maxSum == k: return maxSum
                print("----")
        return maxSum