# [467. Unique Substrings in Wraparound String][title]

<p>We define the string <code>s</code> to be the infinite wraparound string of <code>"abcdefghijklmnopqrstuvwxyz"</code>, so <code>s</code> will look like this:</p>
<ul>
<li><code>"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."</code>.</li>
</ul>
<p>Given a string <code>p</code>, return <em>the number of <strong>unique non-empty substrings</strong> of </em><code>p</code><em> are present in </em><code>s</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> p = "a"
<strong>Output:</strong> 1
Explanation: Only the substring "a" of p is in s.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> p = "cac"
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two substrings ("a", "c") of p in s.
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> p = "zab"
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= p.length &lt;= 10<sup>5</sup></code></li>
<li><code>p</code> consists of lowercase English letters.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/unique-substrings-in-wraparound-string
[me]: https://github.com/bumblebee211196/awesome-python-leetcode