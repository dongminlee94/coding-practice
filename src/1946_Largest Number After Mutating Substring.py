"""
1946. Largest Number After Mutating Substring
https://leetcode.com/problems/largest-number-after-mutating-substring/

Example 1:

Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
Output: "832"
Explanation: Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, "132" becomes "832".
"832" is the largest number that can be created, so return it.

Example 2:

Input: num = "021", change = [9,4,3,5,7,2,1,9,0,6]
Output: "934"
Explanation: Replace the substring "021":
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, "021" becomes "934".
"934" is the largest number that can be created, so return it.

Example 3:

Input: num = "5", change = [1,4,7,5,3,2,5,6,9,4]
Output: "5"
Explanation: "5" is already the largest number that can be created, so return it.
"""

from typing import List


class Solution:
    def maximumNumber1(self, num: str, change: List[int]) -> str:
        """
        TC: O(N^2) / SC: O(N)
        Time Limit Exceeded
        """
        max_num = num
        for i in range(len(num)):
            changed_num = num[:i] + str(change[int(num[i])]) + num[i + 1 :]
            if changed_num >= max_num:
                max_num = changed_num

            for j in range(1, len(num[i + 1 :]) + 1):
                changed_num = (
                    changed_num[: i + j] + str(change[int(num[i + j])]) + changed_num[i + j + 1 :]
                )
                if changed_num >= max_num:
                    max_num = changed_num
                else:
                    break
        return max_num

    def maximumNumber2(self, num: str, change: List[int]) -> str:
        """
        TC: O(N) / SC: O(N)
        Runtime: 284 ms, faster than 66.52%
        Memory Usage: 22.2 MB, less than 49.40%
        """
        num_list = list(num)
        changed = False
        for i in range(len(num_list)):
            if change[int(num_list[i])] > int(num_list[i]):
                num_list[i] = str(change[int(num_list[i])])
                changed = True
            elif changed == True and change[int(num_list[i])] < int(num_list[i]):
                break
        return "".join(num_list)

    def maximumNumber3(self, num: str, change: List[int]) -> str:
        """
        TC: O(N^2) / SC: O(N)
        Runtime: 1324 ms, faster than 6.40%
        Memory Usage: 16.3 MB, less than 63.96%
        """
        changed = False
        for i in range(len(list(num))):
            if str(change[int(num[i])]) > num[i]:
                num = num[:i] + str(change[int(num[i])]) + num[i + 1 :]  # TC: O(N)
                changed = True
            elif changed == True and str(change[int(num[i])]) < num[i]:
                break
        return num
