# [943. Find the Shortest Superstring][title]

<p>Given an array of strings <code>words</code>, return <em>the smallest string that contains each string in</em> <code>words</code> <em>as a substring</em>. If there are multiple valid strings of the smallest length, return <strong>any of them</strong>.</p>
<p>You may assume that no string in <code>words</code> is a substring of another string in <code>words</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["alex","loves","leetcode"]
<strong>Output:</strong> "alexlovesleetcode"
<strong>Explanation:</strong> All permutations of "alex","loves","leetcode" would also be accepted.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["catg","ctaagt","gcta","ttca","atgcatc"]
<strong>Output:</strong> "gctaagttcatgcatc"
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= words.length &lt;= 12</code></li>
<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
<li><code>words[i]</code> consists of lowercase English letters.</li>
<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/find-the-shortest-superstring
[me]: https://github.com/bumblebee211196/awesome-python-leetcode