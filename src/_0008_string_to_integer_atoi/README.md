# [8. String to Integer (atoi)][title]

## Description

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

  * Read in and ignore any leading whitespace.
  * Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
  * Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
  * Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
  * If the integer is out of the 32-bit signed integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2<sup>31</sup> should be clamped to -2<sup>31</sup>, and integers greater than 2<sup>31</sup> - 1 should be clamped to 2<sup>31</sup> - 1.
  * Return the integer as the final result.

**Note:**

  * Only the space character `' '` is considered a whitespace character.
  * Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


**Example 1:**
```text
Input: s = "42"
Output: 42
```

**Example 2:**
```text
Input: s = "   -42"
Output: -42
```

**Example 3:**
```text
Input: s = "4193 with words"
Output: 4193
```

**Example 4:**
```text
Input: s = "words and 987"
Output: 0
```

**Example 5:**
```text
Input: s = "-91283472332"
Output: -2147483648
```

**Tags:** String

If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/string-to-integer-atoi/
[me]: https://github.com/bumblebee211196/awesome-python-leetcode
