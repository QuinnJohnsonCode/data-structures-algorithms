class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t_p = 0
        s_p = 0
        subs = 0
        
        hit = False
        while t_p < len(target):
            if target[t_p] == source[s_p]:
                
                hit = True
                t_p += 1

                if t_p >= len(target):
                    return subs + 1
            

            
            s_p = s_p + 1
            if s_p >= len(source):
                if not hit:
                    return -1
                
                hit = False
                subs += 1
                s_p = 0
  
        return subs
    
# Tests
sol = Solution()
assert sol.shortestWay("abc", "abcbc") == 2
assert sol.shortestWay("abc", "acdbc") == -1
assert sol.shortestWay("xyz", "xzyxz") == 3
assert sol.shortestWay("aaaaa", "aaaaaaaaaaaaa") == 3