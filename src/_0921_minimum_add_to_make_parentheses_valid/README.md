# [921. Minimum Add to Make Parentheses Valid][title]

<p>Given a string <code>s</code> of <code>'('</code> and <code>')'</code> parentheses, we add the minimum number of parentheses ( <code>'('</code> or <code>')'</code>, and in any positions ) so that the resulting parentheses string is valid.</p>
<p>Formally, a parentheses string is valid if and only if:</p>
<ul>
<li>It is the empty string, or</li>
<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>
<p>Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>s = <span id="example-input-1-1">"())"</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>s = <span id="example-input-2-1">"((("</span>
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>s = <span id="example-input-3-1">"()"</span>
<strong>Output: </strong><span id="example-output-3">0</span>
</pre>

<p><strong>Example 4:</strong></p>
<pre><strong>Input: </strong>s = <span id="example-input-4-1">"()))(("</span>
<strong>Output: </strong><span id="example-output-4">4</span></pre>
<p> </p>



<p><strong>Note:</strong></p>
<ol>
<li><code>s.length &lt;= 1000</code></li>
<li><code>s</code> only consists of <code>'('</code> and <code>')'</code> characters.</li>
</ol>



 





If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid
[me]: https://github.com/bumblebee211196/awesome-python-leetcode