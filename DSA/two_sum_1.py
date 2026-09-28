from typing import List

# Brute force: check every pair (i, j)   → O(n²) time, O(1) space
# Hashmap:     one pass, dict of seen    → O(n) time,  O(n) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))        # [1, 2]
    print(sol.twoSum([3, 3], 6))           # [0, 1]
