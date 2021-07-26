# [306. Additive Number][title]

<p>Additive number is a string whose digits can form additive sequence.</p>
<p>A valid additive sequence should contain <b>at least</b> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</p>
<p>Given a string containing only digits <code>'0'-'9'</code>, write a function to determine if it's an additive number.</p>
<p><b>Note:</b> Numbers in the additive sequence <b>cannot</b> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> "112358"
<strong>Output:</strong> true
<strong>Explanation:</strong> The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> "199100199"
<strong>Output:</strong> true
<strong>Explanation:</strong> The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><font face="monospace"><code>num</code> </font>consists only of digits <code>'0'-'9'</code>.</li>
<li><code>1 &lt;= num.length &lt;= 35</code></li>
</ul>
<p><b>Follow up:</b><br/>
How would you handle overflow for very large input integers?</p>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/additive-number
[me]: https://github.com/bumblebee211196/awesome-python-leetcode