# [224. Basic Calculator][title]

<p>Given a string <code>s</code> representing a valid expression, implement a basic calculator to evaluate it, and return <em>the result of the evaluation</em>.</p>
<p><strong>Note:</strong> You are <strong>not</strong> allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "1 + 1"
<strong>Output:</strong> 2
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = " 2-1 + 2 "
<strong>Output:</strong> 3
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(1+(4+5+2)-3)+(6+8)"
<strong>Output:</strong> 23
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
<li><code>s</code> consists of digits, <code>'+'</code>, <code>'-'</code>, <code>'('</code>, <code>')'</code>, and <code>' '</code>.</li>
<li><code>s</code> represents a valid expression.</li>
<li><code>'+'</code> is not used as a unary operation.</li>
<li><code>'-'</code> could be used as a unary operation but it has to be followed by parentheses.</li>
<li>Every number and running calculation will fit in a signed 32-bit integer.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/basic-calculator
[me]: https://github.com/bumblebee211196/awesome-python-leetcode