# [650. 2 Keys Keyboard][title]

<p>There is only one character <code>'A'</code> on the screen of a notepad. You can perform two operations on this notepad for each step:</p>
<ul>
<li>Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).</li>
<li>Paste: You can paste the characters which are copied last time.</li>
</ul>
<p>Given an integer <code>n</code>, return <em>the minimum number of operations to get the character</em> <code>'A'</code> <em>exactly</em> <code>n</code> <em>times on the screen</em>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/2-keys-keyboard
[me]: https://github.com/bumblebee211196/awesome-python-leetcode