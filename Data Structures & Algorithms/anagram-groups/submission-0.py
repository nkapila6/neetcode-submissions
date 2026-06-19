class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # can do the same thing, single forward, maintain hash, 
       # output list of list str from hash

       mem: dict[list[str]]= {}

       for i,s in enumerate(strs):
        key = "".join(sorted(s))
        mem[key] = mem.get(key,[]) + [s]
        
       return list(mem.values())
