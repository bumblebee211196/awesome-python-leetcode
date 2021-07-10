# [12. Integer to Roman][title]

## Description

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. 12 is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

  * I can be placed before `V` (5) and `X` (10) to make 4 and 9. 
  * X can be placed before `L` (50) and `C` (100) to make 40 and 90. 
  * C can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

**Example 1:**
```text
Input: num = 3
Output: "III"
```

**Example 2:**
```text
Input: num = 4
Output: "IV"
```

**Example 3:**
```text
Input: num = 9
Output: "IX"
```

**Example 4:**
```text
Input: num = 58
Output: "LVIII"
```

**Example 5:**
```text
Input: num = 1994
Output: "MCMXCIV"
```

**Tags:** Math, Hash Table, String

If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/integer-to-roman/
[me]: https://github.com/bumblebee211196/awesome-python-leetcode
