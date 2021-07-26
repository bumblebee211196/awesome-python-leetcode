# [903. Valid Permutations for DI Sequence][title]

<p>We are given <code>s</code>, a length <code>n</code> string of characters from the set <code>{'D', 'I'}</code>. (These letters stand for "decreasing" and "increasing".)</p>
<p>A <em>valid permutation</em> is a permutation <code>p[0], p[1], ..., p[n]</code> of integers <code>{0, 1, ..., n}</code>, such that for all <code>i</code>:</p>
<ul>
<li>If <code>s[i] == 'D'</code>, then <code>p[i] &gt; p[i+1]</code>, and;</li>
<li>If <code>s[i] == 'I'</code>, then <code>p[i] &lt; p[i+1]</code>.</li>
</ul>
<p>How many valid permutations are there?  Since the answer may be large, <strong>return your answer modulo </strong><code>10<sup>9</sup> + 7</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>s = <span id="example-input-1-1">"DID"</span>
<strong>Output: </strong><span id="example-output-1">5</span>
<strong>Explanation: </strong>
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= s.length &lt;= 200</code></li>
<li><code>s</code> consists only of characters from the set <code>{'D', 'I'}</code>.</li>
</ol>

<p> </p>



If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/valid-permutations-for-di-sequence
[me]: https://github.com/bumblebee211196/awesome-python-leetcode