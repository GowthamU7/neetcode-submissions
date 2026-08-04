class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        one_len = 0
        for i in nums:
            if i == 1:
                one_len+=1
            else:
                if max_len > one_len : max_len
                else: max_len = one_len
                one_len = 0
        if max_len > one_len : max_len
        else: max_len = one_len
        return max_len