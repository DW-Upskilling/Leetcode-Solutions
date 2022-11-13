class Solution:
    def reverseWords(self, s: str) -> str:
        
        ns = ""
        temp = ""
        for i in s[::-1]:
            if i == ' ' and len(temp):
                ns += temp[::-1] + ' '
                temp = ""

            elif i != ' ':
                temp += i
        
        if temp and temp[-1] == ' ':
            temp = temp[:-1]
        
        if ns and ns[-1] == ' ' and not temp:
            ns = ns[:-1]
        
        return ns + temp[::-1]
            
            