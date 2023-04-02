class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        def isBalanced(st):
            if st.count('0') != st.count('1'):
                return False
            mid = len(st) // 2
            # print(st, len(st), mid, st[:mid].count('1'), st[mid:].count('0'))
            if st[:mid].count('1') > 0 or st[mid:].count('0') > 0:
                return False
            return True
        
        output = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if isBalanced(s[i:j]):
                    # print(i, j, s[i:j])
                    output = max(j-i, output)
        
        return output