# [165. Compare Version Numbers][title]

<p>Given two version numbers, <code>version1</code> and <code>version2</code>, compare them.</p>
<ul>
</ul>
<p>Version numbers consist of <strong>one or more revisions</strong> joined by a dot <code>'.'</code>. Each revision consists of <strong>digits</strong> and may contain leading <strong>zeros</strong>. Every revision contains <strong>at least one character</strong>. Revisions are <strong>0-indexed from left to right</strong>, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example <code>2.5.33</code> and <code>0.1</code> are valid version numbers.</p>
<p>To compare version numbers, compare their revisions in <strong>left-to-right order</strong>. Revisions are compared using their <strong>integer value ignoring any leading zeros</strong>. This means that revisions <code>1</code> and <code>001</code> are considered <strong>equal</strong>. If a version number does not specify a revision at an index, then <strong>treat the revision as <code>0</code></strong>. For example, version <code>1.0</code> is less than version <code>1.1</code> because their revision 0s are the same, but their revision 1s are <code>0</code> and <code>1</code> respectively, and <code>0 &lt; 1</code>.</p>
<p><em>Return the following:</em></p>
<ul>
<li>If <code>version1 &lt; version2</code>, return <code>-1</code>.</li>
<li>If <code>version1 &gt; version2</code>, return <code>1</code>.</li>
<li>Otherwise, return <code>0</code>.</li>
</ul>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> version1 = "1.01", version2 = "1.001"
<strong>Output:</strong> 0
<strong>Explanation:</strong> Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> version1 = "1.0", version2 = "1.0.0"
<strong>Output:</strong> 0
<strong>Explanation:</strong> version1 does not specify revision 2, which means it is treated as "0".
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> version1 = "0.1", version2 = "1.1"
<strong>Output:</strong> -1
<strong>Explanation:</strong> version1's revision 0 is "0", while version2's revision 0 is "1". 0 &lt; 1, so version1 &lt; version2.
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> version1 = "1.0.1", version2 = "1"
<strong>Output:</strong> 1
</pre>
<p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> version1 = "7.5.2.4", version2 = "7.5.3"
<strong>Output:</strong> -1
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= version1.length, version2.length &lt;= 500</code></li>
<li><code>version1</code> and <code>version2</code> only contain digits and <code>'.'</code>.</li>
<li><code>version1</code> and <code>version2</code> <strong>are valid version numbers</strong>.</li>
<li>All the given revisions in <code>version1</code> and <code>version2</code> can be stored in a <strong>32-bit integer</strong>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/compare-version-numbers
[me]: https://github.com/bumblebee211196/awesome-python-leetcode