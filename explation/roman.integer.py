EXPLANATION: Roman to Integer (LeetCode 13)

PROBLEM
Given a valid Roman numeral string s (range 1 to 3999), convert it to an integer.

KEY OBSERVATION
Roman numerals are normally written from largest to smallest, so we ADD the values.
The only exception is the six subtraction cases:
  IV = 4,  IX = 9
  XL = 40, XC = 90
  CD = 400, CM = 900
In each case, a smaller symbol appears BEFORE a larger one, so the smaller one is SUBTRACTED.

THE RULE
For each character:
  - If its value is smaller than the next character's value -> subtract it.
  - Otherwise -> add it.

HOW THE CODE WORKS
1. values = {...}
   Dictionary mapping each symbol to its number, for O(1) lookup.

2. total = 0
   Running result.

3. for i in range(len(s))
   Go through each character by index, so we can look at the next one (i + 1).

4. if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]
   - i + 1 < len(s) makes sure we don't read past the end of the string.
   - If the current symbol is smaller than the next one, it is part of a
     subtraction pair, so: total -= values[s[i]]

5. else: total += values[s[i]]
   Normal case, just add the value.

6. return total

EXAMPLE 1: s = "III"
  I -> next is I (not larger)  -> +1  total = 1
  I -> next is I               -> +1  total = 2
  I -> last character          -> +1  total = 3
  Output: 3

EXAMPLE 2: s = "LVIII"
  L (50) -> next V (5), not larger -> +50  total = 50
  V (5)  -> next I (1), not larger -> +5   total = 55
  I (1)  -> next I                 -> +1   total = 56
  I (1)  -> next I                 -> +1   total = 57
  I (1)  -> last character         -> +1   total = 58
  Output: 58

EXAMPLE 3: s = "MCMXCIV"
  M (1000) -> next C (100), not larger   -> +1000  total = 1000
  C (100)  -> next M (1000), smaller     -> -100   total = 900
  M (1000) -> next X (10), not larger    -> +1000  total = 1900
  X (10)   -> next C (100), smaller      -> -10    total = 1890
  C (100)  -> next I (1), not larger     -> +100   total = 1990
  I (1)    -> next V (5), smaller        -> -1     total = 1989
  V (5)    -> last character             -> +5     total = 1994
  Output: 1994

COMPLEXITY
- Time:  O(n), one pass through the string (n <= 15).
- Space: O(1), the dictionary has a fixed size of 7 entries.

PYTHON VERSION NOTE
This code has no type hints, so it runs on both Python and Python3 in LeetCode.