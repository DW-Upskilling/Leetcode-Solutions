class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        if endWord not in wordList: return []
        
        hashMap = dict()
        for word in wordList:
            hashMap[word] = {
                'word': word,
                'sum': self.sumWord(word),
                'value': self.parseWord(word),
                'path': 1
            }
        if beginWord not in hashMap.keys():
            hashMap[beginWord] = {
                'word': beginWord,
                'sum': self.sumWord(beginWord),
                'value': self.parseWord(beginWord),
                'path': 1
            }
        
        endSum = hashMap[endWord]['sum']
        endValue = hashMap[endWord]['value']

        dictionary = dict()
        queue = [[hashMap[beginWord], 1]]
    
        while len(queue):
            
            # print(queue[0])
            
            e = queue[0][0]
            path = queue[0][1]
            
            # print(e['word'], dictionary)
            
            for index, character in enumerate(e['word']):
                ascii = ord(character)
                hash = ascii * (index+1)

                _value = e['value'] - hash
                _sum = e['sum'] - ascii
                
                key = e['word'][:index] + e['word'][index+1:] + str(_value) + str(_sum)
                
                if key not in dictionary.keys():
                    # print(e['word'], key)
                    dictionary[key] = {e['word']}
                elif e['word'] in dictionary.keys():
                    # print(e['word'], key, dictionary[e['word']], dictionary[key])
                    dictionary[e['word']] = dictionary[e['word']].union(dictionary[key])
                    continue
                    
                if e['word'] not in dictionary.keys():
                    dictionary[e['word']] = dictionary[key].copy()
                
                visited = set()
                for word in hashMap.keys():
                    
                    if word == e['word']: continue

                    element = hashMap[word]
                    # print(element)

                    condition1 = element['value'] - ord(element['word'][index]) * (index+1) == _value
                    condition2 = element['sum'] - ord(element['word'][index]) == _sum
                    
                    _key = word[:index] + word[index+1:] + str(_value) + str(_sum)
                    
                    if condition1 and condition2 and _key == key:
                        # print(e, element, condition1, condition2, _key, key)
                        
                        element['path'] = path + 1
                        
                        dictionary[e['word']].add(word)
                        dictionary[key].add(word)
                        
                        if word not in dictionary.keys():
                            queue.append([element, element['path']])
                            
                        visited.add(word)
                
                for word in visited:
                    dictionary[word] = dictionary[key].copy()
                    # print(e['word'], word, dictionary[word])
                    # del hashMap[word]
            
            # print(e, dictionary[e['word']])
            if e['value'] == endValue and e['sum'] == endSum and endWord == e['word']:
                break
            
            if e['word'] in hashMap.keys(): del hashMap[e['word']]
            
            queue.pop(0)
            # print(e, queue) 

        output = []
        npath = []
        # print(queue)
        # print(dictionary)
        if len(queue) > 0:
            for i in dictionary[endWord]:
                if i == endWord: continue
                path = [i, endWord]
                p = self.findShortestPath(dictionary, beginWord, i, queue[0][1] - 1, path)
                # print(p)
                npath.extend(p)
        
        return npath
    
    def findShortestPath(self, d, s, e, dist, path):
        
        if dist == 1 and s != e: 
            # print(path)
            return []
        elif dist == 1: return [path]
        
        # print(s, path, dist)
        npath = []
        # print(e, d[e])
        for i in d[e]:
            if i == e or i in path: continue
            p = [i] + path 
            # print(p, dist, i, e)
            p = self.findShortestPath(d, s, i, dist - 1, p)
            if len(p) < 1: continue
            npath.extend(p)

        # print(s, npath)
        return npath
            
    def parseWord(self, word):
        result = 0
        for i, c in enumerate(word):
            _t = ord(c) * (i+1)
            result += _t
            
        return result
    
    def sumWord(self, word):
        result = 0
        for i, c in enumerate(word):
            result += ord(c)
            
        return result
            