class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lib = {}
        res= [0,0]
        for i in range(len(nums)):
            if((target - nums[i]) in lib):
                res[0] = lib[target-nums[i]]
                res[1]=i
                return res
            else:
                lib[nums[i]] = i
        print(lib)
        