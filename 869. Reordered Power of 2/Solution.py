class Solution:
    # power of 2 value under 10**9
    # MAX_2POWER = 1073741824
    def reorderedPowerOf2(self, n: int) -> bool:
        # find no. of digits in the 'n'
        digits = 0
        temp = n
        counts = dict()
        while temp > 0:
            # print(temp)
            d = str(temp % 10)
            if d not in counts.keys():
                counts[d] = 0
            counts[d] += 1
            temp //= 10
            digits += 1

        _p = 0
        _v = 1
        _d = 1
        powers = [2 ** 3, 2 ** 4]
        while _v < n and digits > _d:
            if _p % 10 == 0:
                _p += 4
                _v *= powers[1]
            else:
                _p += 3
                _v *= powers[0]
            _d += 1

        end = 0
        if _p % 10 == 0:
            end = _p + 4
        else:
            end = _p + 3
        # print(_p, _v, _d, end)

        for i in range(_p, end):
            _n = counts.copy()
            flg = True
            for i in str(_v):
                if i in _n.keys() and _n[i] > 0:
                    _n[i] -= 1
                else:
                    flg = False
                    break
            
            if flg: return True
            
            _v *= 2

        return False
        