class Solution:
    def trap(self, height: list[int]) -> int:
        lmax = [height[0]]
        rmax = [height[-1]]

        for i in height[1::]:
            lmax.append(max(lmax[-1], i))
        
        for i in height[-2::-1]:
            rmax.insert(0, max(rmax[0], i))
        # print(lmax, rmax)
        output = 0
        for i in range(1, len(height)-1):
            output += min(lmax[i], rmax[i]) - height[i]
            # print(output, lmax[i], rmax[i], height[i])

        return output
