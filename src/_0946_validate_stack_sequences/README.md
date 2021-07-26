# [946. Validate Stack Sequences][title]

<p>Given two sequences <code>pushed</code> and <code>popped</code> <strong>with distinct values</strong>, return <code>true</code> if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.</p>
<p> </p>

<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>pushed = <span id="example-input-1-1">[1,2,3,4,5]</span>, popped = <span id="example-input-1-2">[4,5,3,2,1]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -&gt; 4,
push(5), pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>pushed = <span id="example-input-2-1">[1,2,3,4,5]</span>, popped = <span id="example-input-2-2">[4,3,5,1,2]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>1 cannot be popped before 2.
</pre>


<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>0 &lt;= pushed.length == popped.length &lt;= 1000</code></li>
<li><code>0 &lt;= pushed[i], popped[i] &lt; 1000</code></li>
<li><code>pushed</code> is a permutation of <code>popped</code>.</li>
<li><code>pushed</code> and <code>popped</code> have distinct values.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/validate-stack-sequences
[me]: https://github.com/bumblebee211196/awesome-python-leetcode