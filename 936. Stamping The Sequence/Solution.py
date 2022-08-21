class Solution:
    # Approach is replace all the characters in the target with '?'
    # More like bottom-up approach
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        # print("---") 
        output = []
        count = 0

        # Loops runs till the target is filled with '?'
        while count < len(target):
            indices = []

            # Partitions traget so it can be compared to stamp
            for i in range(len(target) - len(stamp) + 1):    
                _target = target[i: i+len(stamp)]
                flg = True
                cng = False
                # Checking if there any characters to be replaced
                # If all characters are already '?' then ingore
                # If any character is not matched with stamp or is not a '?' will be ignored
                for j in range(len(stamp)):
                    if _target[j] == '?': continue 
                    if _target[j] == stamp[j]:
                        cng = True
                        continue
                    flg = False
                    break
                # print(i, _target, stamp, flg, cng)
                if not cng: continue
                if not flg: continue
                indices.append(i)

            # If there are partitions to be replaced with '?' then return []
            # print("indices:", indices)
            if not len(indices): return []

            # Replaced target with '?' of the found index
            for index in indices:
                ntarget = target[:index:]
                for i in range(index, index + len(stamp)):
                    if target[i] != '?': count += 1
                    ntarget += '?'
                ntarget += target[index + len(stamp)::]
                target = ntarget

            output = indices + output
        # print(target)
        return output
    