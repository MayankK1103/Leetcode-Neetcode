import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        zero_cnt = 0
        total = math.prod(nums)
        
        for num in nums:
            if num != 0:
                continue
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        
        if zero_cnt == 1:
            index = nums.index(0)
            copy = nums[0:index] + nums[index+1:]
            temp_total = math.prod(copy)
            for i in range(len(nums)):
                if i == index:
                    output[i] = temp_total
                else:
                    output[i] == 0
        
        if zero_cnt == 0:
            for i in range(len(nums)):
                output[i] = int(total/nums[i])
        
        return output