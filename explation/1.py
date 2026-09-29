EXPLANATION: Two Sum (LeetCode 1)

PROBLEM
Given an array nums and an integer target, return the indices of the two numbers that add up to target. Exactly one solution exists, and the same element can't be used twice.

BRUTE FORCE (WHY WE DON'T USE IT)
Check every pair with two nested loops. That is O(n^2) time, which is slow for large inputs.

THE IDEA: HASH MAP
For each number, the partner we need is:
  complement = target - num
Instead of searching the array for it, we remember every number we've already seen in a dictionary, so the lookup takes O(1).

  seen = { number : index }

HOW THE CODE WORKS
1. seen = {}
   Empty dictionary that stores numbers we've passed and their indices.

2. for i, num in enumerate(nums)
   Loop through the array, getting both the index (i) and the value (num).

3. complement = target - num
   The value that would complete the pair with the current number.

4. if complement in seen: return [seen[complement], i]
   If the complement was already seen earlier, we found the pair.
   seen[complement] is its index, and i is the current index.

5. seen[num] = i
   Otherwise, store the current number and its index for future lookups.
   This is done AFTER the check, so the same element is never used twice.

EXAMPLE: nums = [2, 7, 11, 15], target = 9
  i=0, num=2:  complement = 7, seen = {}          -> not found, seen = {2: 0}
  i=1, num=7:  complement = 2, seen = {2: 0}      -> found!
  Return [seen[2], 1] = [0, 1]

EXAMPLE 2: nums = [3, 2, 4], target = 6
  i=0, num=3:  complement = 3, seen = {}          -> not found, seen = {3: 0}
  i=1, num=2:  complement = 4, seen = {3: 0}      -> not found, seen = {3: 0, 2: 1}
  i=2, num=4:  complement = 2, seen = {3:0, 2:1}  -> found!
  Return [1, 2]

EXAMPLE 3: nums = [3, 3], target = 6
  i=0, num=3:  complement = 3, seen = {}          -> not found, seen = {3: 0}
  i=1, num=3:  complement = 3, seen = {3: 0}      -> found!
  Return [0, 1]
  (Works because we check BEFORE storing the current number.)

COMPLEXITY
- Time:  O(n), one pass through the array with O(1) dictionary lookups.
- Space: O(n), the dictionary can hold up to n numbers.

PYTHON VERSION NOTE
This code has no type hints, so it runs on both Python and Python3 in LeetCode.