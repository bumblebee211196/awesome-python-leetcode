# [830. Positions of Large Groups][title]

<p>In a string <code><font face="monospace">s</font></code> of lowercase letters, these letters form consecutive groups of the same character.</p>
<p>For example, a string like <code>s = "abbxxxxzyy"</code> has the groups <code>"a"</code>, <code>"bb"</code>, <code>"xxxx"</code>, <code>"z"</code>, and <code>"yy"</code>.</p>
<p>A group is identified by an interval <code>[start, end]</code>, where <code>start</code> and <code>end</code> denote the start and end indices (inclusive) of the group. In the above example, <code>"xxxx"</code> has the interval <code>[3,6]</code>.</p>
<p>A group is considered <strong>large</strong> if it has 3 or more characters.</p>
<p>Return <em>the intervals of every <strong>large</strong> group sorted in <strong>increasing order by start index</strong></em>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abbxxxxzzy"
<strong>Output:</strong> [[3,6]]
<strong>Explanation</strong>: <code>"xxxx" is the only </code>large group with start index 3 and end index 6.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> []
<strong>Explanation</strong>: We have groups "a", "b", and "c", none of which are large groups.
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "abcdddeeeeaabbbcd"
<strong>Output:</strong> [[3,5],[6,9],[12,14]]
<strong>Explanation</strong>: The large groups are "ddd", "eeee", and "bbb".
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> []
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s.length &lt;= 1000</code></li>
<li><code>s</code> contains lower-case English letters only.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/positions-of-large-groups
[me]: https://github.com/bumblebee211196/awesome-python-leetcode