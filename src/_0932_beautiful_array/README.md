# [932. Beautiful Array][title]

<p>For some fixed <code>n</code>, an array <code>nums</code> is <em>beautiful</em> if it is a permutation of the integers <code>1, 2, ..., n</code>, such that:</p>
<p>For every <code>i &lt; j</code>, there is <strong>no</strong> <code>k</code> with <code>i &lt; k &lt; j</code> such that <code>nums[k] * 2 = nums[i] + nums[j]</code>.</p>
<p>Given <code>n</code>, return <strong>any</strong> beautiful array <code>nums</code>.  (It is guaranteed that one exists.)</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>n = <span id="example-input-1-1">4</span>
<strong>Output: </strong><span id="example-output-1">[2,1,4,3]</span>
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>n = <span id="example-input-2-1">5</span>
<strong>Output: </strong><span>[3,1,2,5,4]</span></pre>
<p> </p>

<p><strong>Note:</strong></p>
<ul>
<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

 



If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/beautiful-array
[me]: https://github.com/bumblebee211196/awesome-python-leetcode