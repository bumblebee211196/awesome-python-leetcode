# [481. Magical String][title]

<p>A magical string <code>s</code> consists of only <code>'1'</code> and <code>'2'</code> and obeys the following rules:</p>
<ul>
<li>The string s is magical because concatenating the number of contiguous occurrences of characters <code>'1'</code> and <code>'2'</code> generates the string <code>s</code> itself.</li>
</ul>
<p>The first few elements of <code>s</code> is <code>s = "1221121221221121122……"</code>. If we group the consecutive <code>1</code>'s and <code>2</code>'s in s, it will be <code>"1 22 11 2 1 22 1 22 11 2 11 22 ......"</code> and the occurrences of <code>1</code>'s or <code>2</code>'s in each group are <code>"1 2 2 1 1 2 1 2 2 1 2 2 ......"</code>. You can see that the occurrence sequence is <code>s</code> itself.</p>
<p>Given an integer <code>n</code>, return the number of <code>1</code>'s in the first <code>n</code> number in the magical string <code>s</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 6
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first 6 elements of magical string s is "12211" and it contains three 1's, so return 3.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/magical-string
[me]: https://github.com/bumblebee211196/awesome-python-leetcode