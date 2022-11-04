class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        buffer = []
        ns = []
        for i in s:
            if i.lower() in vowels:
                buffer.append(i)
            ns.append(i)
                
        for i in range(len(s)):
            if ns[i].lower() in vowels:
                ns[i] = buffer[-1]
                buffer.pop()
                
        return "".join(ns)