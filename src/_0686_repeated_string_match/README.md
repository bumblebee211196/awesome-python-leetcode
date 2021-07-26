# [686. Repeated String Match][title]

<p>Given two strings <code>a</code> and <code>b</code>, return the minimum number of times you should repeat string <code>a</code> so that string <code>b</code> is a substring of it. If it is impossible for <code>b</code>​​​​​​ to be a substring of <code>a</code> after repeating it, return <code>-1</code>.</p>
<p><strong>Notice:</strong> string <code>"abc"</code> repeated 0 times is <code>""</code>,  repeated 1 time is <code>"abc"</code> and repeated 2 times is <code>"abcabc"</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> a = "abcd", b = "cdabcdab"
<strong>Output:</strong> 3
<strong>Explanation:</strong> We return 3 because by repeating a three times "ab<strong>cdabcdab</strong>cd", b is a substring of it.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> a = "a", b = "aa"
<strong>Output:</strong> 2
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> a = "a", b = "a"
<strong>Output:</strong> 1
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> a = "abc", b = "wxyz"
<strong>Output:</strong> -1
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= a.length &lt;= 10<sup>4</sup></code></li>
<li><code>1 &lt;= b.length &lt;= 10<sup>4</sup></code></li>
<li><code>a</code> and <code>b</code> consist of lower-case English letters.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/repeated-string-match
[me]: https://github.com/bumblebee211196/awesome-python-leetcode