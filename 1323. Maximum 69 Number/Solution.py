class Solution:
    def maximum69Number (self, num: int) -> int:
        
        output = 0
        flg = False
        for i in str(num):
            if not flg and i == '6':
                flg = True
                i = '9'

            output = output * 10 + int(i)
            
        return output