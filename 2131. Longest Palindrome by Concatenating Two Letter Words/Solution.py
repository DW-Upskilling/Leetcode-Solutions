class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        
        hashMap = dict()
        
        output = 0
        
        for w in words:
            
            if w in hashMap.keys():
                hashMap[w][0] += 1
            elif w[::-1] in hashMap.keys():
                hashMap[w[::-1]][1] += 1
            else:
                hashMap[w] = [1, 0, w[0] == w[1]]
            
        # print(hashMap)
        add = 0
        for k in hashMap.keys():
            _v = min(hashMap[k][0], hashMap[k][1])
            
            if hashMap[k][2]:
                _v = max(hashMap[k][0], hashMap[k][1]) // 2
                if not add:
                    add = max(hashMap[k][0], hashMap[k][1]) % 2
            # print(k, _v, add)
            output += _v * 4
        
        return output + add * 2
            
            
            