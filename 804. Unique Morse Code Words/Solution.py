MORSE_CODES = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        hashMap = dict()
        for word in words:
            code = ""
            for ch in word:
                index = ord(ch) - 97
                code += MORSE_CODES[index]
            
            if code not in hashMap.keys():
                hashMap[code] = 0
            hashMap[code] += 1
        
        return len(hashMap.keys())
            