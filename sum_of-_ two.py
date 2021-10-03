nums =[3,2,4]
target = 6
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myArrayLen = len(nums)
        i = 0
        j = (i + 1)
        for i in range(0, myArrayLen):
            for j in range(i+1, myArrayLen):
                if nums[j] == target - nums[i]:
                    return [i,j]
