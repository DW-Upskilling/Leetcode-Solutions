class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        d = dict()
        
        output = []
        def getCounts(s):
            counts = dict()
            for c in s:
                if c not in counts.keys():
                    counts[c] = 0
                counts[c] += 1
            return counts
        
        for s in strs:
            counts = getCounts(s)
            
            ref = d
            for k in sorted(counts.keys()):
                k = str(counts[k]) + k
                if k in ref.keys():
                    ref = ref[k]
                else:
                    ref[k] = dict()
                    ref = ref[k]
            if '_values' in ref.keys():
                ref['_values'].append(s)
            else:
                ref['_values'] = [s]
                output.append(ref['_values'])
        
        return output
            