# [770. Basic Calculator IV][title]

<p>Given an expression such as <code>expression = "e + 8 - a + 5"</code> and an evaluation map such as <code>{"e": 1}</code> (given in terms of <code>evalvars = ["e"]</code> and <code>evalints = [1]</code>), return a list of tokens representing the simplified expression, such as <code>["-1*a","14"]</code></p>
<ul>
<li>An expression alternates chunks and symbols, with a space separating each chunk and symbol.</li>
<li>A chunk is either an expression in parentheses, a variable, or a non-negative integer.</li>
<li>A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like <code>"2x"</code> or <code>"-x"</code>.</li>
</ul>
<p>Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.</p>
<ul>
<li>For example, <code>expression = "1 + 2 * 3"</code> has an answer of <code>["7"]</code>.</li>
</ul>
<p>The format of the output is as follows:</p>
<ul>
<li>For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
	<ul>
<li>For example, we would never write a term like <code>"b*a*c"</code>, only <code>"a*b*c"</code>.</li>
</ul>
</li>
<li>Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
	<ul>
<li>For example, <code>"a*a*b*c"</code> has degree <code>4</code>.</li>
</ul>
</li>
<li>The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.</li>
<li>An example of a well-formatted answer is <code>["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]</code>.</li>
<li>Terms (including constant terms) with coefficient <code>0</code> are not included.
	<ul>
<li>For example, an expression of <code>"0"</code> has an output of <code>[]</code>.</li>
</ul>
</li>
</ul>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
<strong>Output:</strong> ["-1*a","14"]
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
<strong>Output:</strong> ["-1*pressure","5"]
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
<strong>Output:</strong> ["1*e*e","-64"]
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
<strong>Output:</strong> ["5*a*b*c"]
</pre>
<p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", evalvars = [], evalints = []
<strong>Output:</strong> ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= expression.length &lt;= 250</code></li>
<li><code>expression</code> consists of lowercase English letters, digits, <code>'+'</code>, <code>'-'</code>, <code>'*'</code>, <code>'('</code>, <code>')'</code>, <code>' '</code>.</li>
<li><code>expression</code> does not contain any leading or trailing spaces.</li>
<li>All the tokens in <code>expression</code> are separated by a single space.</li>
<li><code>0 &lt;= evalvars.length &lt;= 100</code></li>
<li><code>1 &lt;= evalvars[i].length &lt;= 20</code></li>
<li><code>evalvars[i]</code> consists of lowercase English letters.</li>
<li><code>evalints.length == evalvars.length</code></li>
<li><code>-100 &lt;= evalints[i] &lt;= 100</code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/basic-calculator-iv
[me]: https://github.com/bumblebee211196/awesome-python-leetcode