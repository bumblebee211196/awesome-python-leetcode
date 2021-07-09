# [10. Regular Expression Matching][title]

## Description

Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'` and `'*'` where: 

  * `'.'` Matches any single character.​​​​
  * `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

**Example 1:**
```text
Input: s = "aa", p = "a"
Output: false
```

**Example 2:**
```text
Input: s = "aa", p = "a*"
Output: true
```

**Example 3:**
```text
Input: s = "ab", p = ".*"
Output: true
```

**Example 4:**
```text
Input: s = "aab", p = "c*a*b"
Output: true
```

**Example 5:**
```text
Input: s = "mississippi", p = "mis*is*p*."
Output: false
```

**Tags:** String, Dynamic Programming, Recursion

If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/regular-expression-matching/
[me]: https://github.com/bumblebee211196/awesome-python-leetcode
