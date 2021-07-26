# [664. Strange Printer][title]

<p>There is a strange printer with the following two special properties:</p>
<ul>
<li>The printer can only print a sequence of <strong>the same character</strong> each time.</li>
<li>At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.</li>
</ul>
<p>Given a string <code>s</code>, return <em>the minimum number of turns the printer needed to print it</em>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aaabbb"
<strong>Output:</strong> 2
<strong>Explanation:</strong> Print "aaa" first and then print "bbb".
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> 2
<strong>Explanation:</strong> Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s.length &lt;= 100</code></li>
<li><code>s</code> consists of lowercase English letters.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/strange-printer
[me]: https://github.com/bumblebee211196/awesome-python-leetcode