class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {} # can be default dicct with list data structure
        # keys with the sorted version of the string and the values
        # being the list of the words that match the anagram

        for s in strs:
            key = "".join(sorted(s))
            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)
        
        return list(res.values())



        
       
        

        