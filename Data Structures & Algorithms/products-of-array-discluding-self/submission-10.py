import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = math.prod(nums)
        output = []
        
        
        if total != 0:
            for i in range(len(nums)):
                output.append(int((total / nums[i])))
        
        else:
            for i in range(len(nums)):
                copy = nums[0:i] + nums[i+1:]
                temp_total = math.prod(copy)
                output.append(temp_total)



        return output