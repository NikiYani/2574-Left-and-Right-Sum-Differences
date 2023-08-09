class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = 0

        for i in range(0, len(nums)) :
            rightSum += nums[i]

        res = []
        rightSum -= nums[0]
        res.append(abs(leftSum - rightSum))

        for i in range(1, len(nums)) :
            rightSum -= nums[i]
            leftSum += nums[i - 1]
            res.append(abs(leftSum - rightSum))

        return res