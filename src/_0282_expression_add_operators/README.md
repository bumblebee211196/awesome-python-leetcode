# [282. Expression Add Operators][title]

<p>Given a string <code>num</code> that contains only digits and an integer <code>target</code>, return <em>all possibilities to add the binary operators</em> <code>'+'</code>, <code>'-'</code>, <em>or</em> <code>'*'</code> <em>between the digits of</em> <code>num</code> <em>so that the resultant expression evaluates to the</em> <code>target</code> <em>value</em>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> num = "123", target = 6
<strong>Output:</strong> ["1*2*3","1+2+3"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> num = "232", target = 8
<strong>Output:</strong> ["2*3+2","2+3*2"]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> num = "105", target = 5
<strong>Output:</strong> ["1*0+5","10-5"]
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> num = "00", target = 0
<strong>Output:</strong> ["0*0","0+0","0-0"]
</pre><p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> num = "3456237490", target = 9191
<strong>Output:</strong> []
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= num.length &lt;= 10</code></li>
<li><code>num</code> consists of only digits.</li>
<li><code>-2<sup>31</sup> &lt;= target &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/expression-add-operators
[me]: https://github.com/bumblebee211196/awesome-python-leetcode