class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs_map = {}
        res = []
        for st in strs:
            tmp_st = "".join(sorted(st))
            tmp_st
            if tmp_st in hs_map:
                hs_map[tmp_st].append(st)
            else:
                hs_map[tmp_st] = [st]
        

        for key in hs_map:
            res.append(hs_map[key])
        return res