class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        m = 1
        curr = 1
        prev = ord(s[0])
        
        for i in s[1::]:
            
            _t = ord(i)
            
            # print(prev, _t)
            if prev + 1 == _t:
                curr += 1
            else:
                curr = 1
                
            prev = _t
            if curr > m:
                m = curr
                
        return m