# 2574. Left and Right Sum Differences

Given a 0-indexed integer array nums, find a 0-indexed integer array answer where: </br>

answer.length == nums.length. </br>
answer[i] = |leftSum[i] - rightSum[i]|. </br>
Where: </br>

leftSum[i] is the sum of elements to the left of the index i in the array nums. </br>
If there is no such element, leftSum[i] = 0. </br>
rightSum[i] is the sum of elements to the right of the index i in the array nums.  </br>
If there is no such element, rightSum[i] = 0. </br>
Return the array answer. </br>

## Example 1:

Input: nums = [10,4,8,3] </br>
Output: [15,1,11,22] </br>
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0]. </br>
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22]. </br>

## Example 2:

Input: nums = [1] </br>
Output: [0] </br>
Explanation: The array leftSum is [0] and the array rightSum is [0]. </br>
The array answer is [|0 - 0|] = [0]. </br>

## Constraints:

1 <= nums.length <= 1000 </br>
1 <= nums[i] <= 105 </br>
