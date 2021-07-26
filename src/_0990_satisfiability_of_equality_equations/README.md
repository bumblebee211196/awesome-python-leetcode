# [990. Satisfiability of Equality Equations][title]

<p>Given an array <font face="monospace">equations</font> of strings that represent relationships between variables, each string <code>equations[i]</code> has length <code>4</code> and takes one of two different forms: <code>"a==b"</code> or <code>"a!=b"</code>.  Here, <code>a</code> and <code>b</code> are lowercase letters (not necessarily different) that represent one-letter variable names.</p>
<p>Return <code>true</code> if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.</p>
<p> </p>
<ol>
</ol>

<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong><span id="example-input-1-1">["a==b","b!=a"]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
<strong>Explanation: </strong>If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong><span id="example-input-2-1">["b==a","a==b"]</span>
<strong>Output: </strong><span id="example-output-2">true</span>
<strong>Explanation: </strong>We could assign a = 1 and b = 1 to satisfy both equations.
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong><span id="example-input-3-1">["a==b","b==c","a==c"]</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>

<p><strong>Example 4:</strong></p>
<pre><strong>Input: </strong><span id="example-input-4-1">["a==b","b!=c","c==a"]</span>
<strong>Output: </strong><span id="example-output-4">false</span>
</pre>

<p><strong>Example 5:</strong></p>
<pre><strong>Input: </strong><span id="example-input-5-1">["c==c","b==d","x!=z"]</span>
<strong>Output: </strong><span id="example-output-5">true</span>
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= equations.length &lt;= 500</code></li>
<li><code>equations[i].length == 4</code></li>
<li><code>equations[i][0]</code> and <code>equations[i][3]</code> are lowercase letters</li>
<li><code>equations[i][1]</code> is either <code>'='</code> or <code>'!'</code></li>
<li><code>equations[i][2]</code> is <code>'='</code></li>
</ol>







If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/satisfiability-of-equality-equations
[me]: https://github.com/bumblebee211196/awesome-python-leetcode