class Solution:
    def isValid(self, s: str) -> bool:
        maps, st = {
                ")":"(",
                "]":"[",
                "}":"{",
                }, []

        for ch in s:
            if ch in maps:
                ele = st.pop() if st else "#"

                if maps[ch] != ele:
                    return False
            else:
                st.append(ch)
        
        return len(st) == 0
            
