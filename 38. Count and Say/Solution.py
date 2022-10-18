class Solution:
    def countAndSay(self, n: int) -> str:
        
        def helper(n, s):    
            if not n: return s
            
            ns = ""
            prev = s[0]
            val = 1
            for i in s[1:]:
                if prev == i:
                    val += 1
                elif val:
                    ns += str(val) + prev
                    val = 1
                    prev = i
                # print(prev, i, ns, val)
            if val:
                ns += str(val) + prev
            
            
            return helper(n-1, ns)
        
        return helper(n-1, "1")