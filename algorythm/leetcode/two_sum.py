from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,fnum in enumerate(nums):
            for jdx in [x for x in range(len(nums)) if x != idx]:
                if fnum + nums[jdx] == target:
                    return [idx,jdx]
        

sol = Solution()
print(sol.twoSum([2,7,11,15],9))