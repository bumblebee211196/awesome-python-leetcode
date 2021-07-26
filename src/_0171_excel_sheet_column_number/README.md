# [171. Excel Sheet Column Number][title]

<p>Given a string <code>columnTitle</code> that represents the column title as appear in an Excel sheet, return <em>its corresponding column number</em>.</p>
<p>For example:</p>
<pre>A -&gt; 1
B -&gt; 2
C -&gt; 3
...
Z -&gt; 26
AA -&gt; 27
AB -&gt; 28 
...
</pre>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> columnTitle = "A"
<strong>Output:</strong> 1
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> columnTitle = "AB"
<strong>Output:</strong> 28
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> columnTitle = "ZY"
<strong>Output:</strong> 701
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> columnTitle = "FXSHRXW"
<strong>Output:</strong> 2147483647
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= columnTitle.length &lt;= 7</code></li>
<li><code>columnTitle</code> consists only of uppercase English letters.</li>
<li><code>columnTitle</code> is in the range <code>["A", "FXSHRXW"]</code>.</li>
</ul>

If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/excel-sheet-column-number
[me]: https://github.com/bumblebee211196/awesome-python-leetcode