# [592. Fraction Addition and Subtraction][title]

<p>Given a string <code>expression</code> representing an expression of fraction addition and subtraction, return the calculation result in string format.</p>
<p>The final result should be an <a href="https://en.wikipedia.org/wiki/Irreducible_fraction" target="_blank">irreducible fraction</a>. If your final result is an integer, say <code>2</code>, you need to change it to the format of a fraction that has a denominator <code>1</code>. So in this case, <code>2</code> should be converted to <code>2/1</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> expression = "-1/2+1/2"
<strong>Output:</strong> "0/1"
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> expression = "-1/2+1/2+1/3"
<strong>Output:</strong> "1/3"
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> expression = "1/3-1/2"
<strong>Output:</strong> "-1/6"
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> expression = "5/3+1/3"
<strong>Output:</strong> "2/1"
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li>The input string only contains <code>'0'</code> to <code>'9'</code>, <code>'/'</code>, <code>'+'</code> and <code>'-'</code>. So does the output.</li>
<li>Each fraction (input and output) has the format <code>±numerator/denominator</code>. If the first input fraction or the output is positive, then <code>'+'</code> will be omitted.</li>
<li>The input only contains valid <b>irreducible fractions</b>, where the <b>numerator</b> and <b>denominator</b> of each fraction will always be in the range <code>[1, 10]</code>. If the denominator is <code>1</code>, it means this fraction is actually an integer in a fraction format defined above.</li>
<li>The number of given fractions will be in the range <code>[1, 10]</code>.</li>
<li>The numerator and denominator of the <b>final result</b> are guaranteed to be valid and in the range of <strong>32-bit</strong> int.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/fraction-addition-and-subtraction
[me]: https://github.com/bumblebee211196/awesome-python-leetcode