class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive approach is two nested loops that become O(n^2)
        # How to make O(n), hashset or hashmap? but what would
        # the logic be? Maybe if target - i is found in the set
        # then return the index

        num_set = set(nums)
        for i in num_set:
            if (target - i) in num_set:
                i, j = i, target - i
                break

        if nums.index(i) < nums.index(j):
            return [nums.index(i), nums.index(j)]
        elif nums.index(i) > nums.index(j):
            return [nums.index(j), nums.index(i)]
        else:
            return [nums.index(i), nums.index(j, nums.index(i) + 1)]
        