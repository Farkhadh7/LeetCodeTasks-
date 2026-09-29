Explanation in Human Speech

Think of it like this: you have a sorted row of numbered cards, and you want to keep only one card of each number at the front of the row. You don't care what's left over at the back.

The key fact: the array is sorted, so duplicates are always sitting right next to each other. That means to know if a number is new, you only need to compare it with the one just before it.

Two pointers:

i is the reader. It walks through the whole array from left to right.
k is the writer. It marks the spot where the next unique number should be placed. It also happens to equal the count of unique numbers found so far.

Why k starts at 1: the very first number is always unique (nothing came before it), so it's already in the right place. The next free spot is index 1.

The loop: for each number at i:

If nums[i] != nums[i - 1], it's a new value. Copy it to nums[k] and move k forward by one.
If it's the same as the previous one, it's a duplicate. Skip it and do nothing.

At the end, k is the number of unique elements, and the first k slots of nums hold them in order.

Walking through Example 1: nums = [1,1,2]

k = 1.
i = 1: 1 == 1, duplicate, skip.
i = 2: 2 != 1, new. Write nums[1] = 2, so k = 2.
Array is now [1,2,2], return 2. The first two elements are 1, 2. ✅

Walking through Example 2: nums = [0,0,1,1,1,2,2,3,3,4]

k = 1.
i = 1: 0 == 0, skip.
i = 2: 1 != 0, write nums[1] = 1, k = 2.
i = 3, 4: 1 == 1, skip.
i = 5: 2 != 1, write nums[2] = 2, k = 3.
i = 6: 2 == 2, skip.
i = 7: 3 != 2, write nums[3] = 3, k = 4.
i = 8: 3 == 3, skip.
i = 9: 4 != 3, write nums[4] = 4, k = 5.
Array starts with [0,1,2,3,4,...], return 5. ✅

Edge case: if the array has just one element, the loop never runs and we return 1, which is correct. The constraints guarantee at least one element, so we don't need an empty check.