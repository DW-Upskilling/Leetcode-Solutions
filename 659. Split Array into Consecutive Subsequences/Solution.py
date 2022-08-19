class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        l = len(nums)
        counts = dict()

        for n in nums:
            if n not in counts.keys():
                counts[n] = 0
            counts[n] += 1
        # print(counts)

        seq = dict()
        for n in nums:
            # print(seq, counts)
            if not counts[n]:
                continue

            if n-1 in seq.keys() and seq[n-1] > 0:
                seq[n-1] -= 1
                if n not in seq.keys():
                    seq[n] = 0
                seq[n] += 1
            else:
                if n+1 not in counts.keys() or n+2 not in counts.keys(): return False
                if not counts[n+1] or not counts[n+2]: return False
                counts[n+1] -= 1
                counts[n+2] -= 1
                if n+2 not in seq.keys():
                    seq[n+2] = 0
                seq[n+2] += 1

            counts[n] -= 1
        
        return True