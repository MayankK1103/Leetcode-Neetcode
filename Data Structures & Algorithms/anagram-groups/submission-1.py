class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {} # can be default dicct with list data structure
        # keys with the sorted version of the string and the values
        # being the list of the words that match the anagram

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            if tuple(count) not in res:
                res[tuple(count)] = [s]
            else:
                res[tuple(count)].append(s)
        
        return list(res.values())



        
       
        

        