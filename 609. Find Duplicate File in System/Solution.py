class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        
        m = dict()
        
        getCharValue = lambda i, x, l: (ord(x) * 10**i) - l 
        
        for p in paths:
            
            temp = p.split(" ")
            path = temp[0]
            files = temp[1:]
            # print(path, files)
            for file in files:
                
                temp = file.split("(")
                name = temp[0]
                content = temp[1].split(")")[0]
                value = sum([getCharValue(i, c, len(content)) for i, c in enumerate(content)])
                # print(name, content, value)
                
                if value not in m.keys():
                    m[value] = []
                    
                m[value].append(path + "/" + name)
        
        output = []
        for k in m.keys():
            if len(m[k]) > 1:
                output.append(m[k])
        return output