# [910. Smallest Range II][title]

<p>Given an array <code>nums</code> of integers, for each integer <code>nums[i]</code> we need to choose <strong>either <code>x = -k</code> or <code>x = k</code></strong>, and add <code>x</code> to <code>nums[i] <strong>(only once)</strong></code>.</p>
<p>After this process, we have some array <code>result</code>.</p>
<p>Return the smallest possible difference between the maximum value of <code>result</code> and the minimum value of <code>result</code>.</p>
<p> </p>
<ol>
</ol>

<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>nums = <span id="example-input-1-1">[1]</span>, k = <span id="example-input-1-2">0</span>
<strong>Output: </strong><span id="example-output-1">0</span>
<span><strong>Explanation</strong>: result = [1]</span>
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>nums = <span id="example-input-2-1">[0,10]</span>, k = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span><strong>Explanation</strong>: result = [2,8]</span>
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>nums = <span id="example-input-3-1">[1,3,6]</span>, k = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<span><strong>Explanation</strong>: result = [4,6,3]</span>
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= nums.length &lt;= 10000</code></li>
<li><code>0 &lt;= nums[i] &lt;= 10000</code></li>
<li><code>0 &lt;= k &lt;= 10000</code></li>
</ol>





If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/smallest-range-ii
[me]: https://github.com/bumblebee211196/awesome-python-leetcode