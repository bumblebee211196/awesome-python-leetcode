# [915. Partition Array into Disjoint Intervals][title]

<p>Given an array <code>nums</code>, partition it into two (contiguous) subarrays <code>left</code> and <code>right</code> so that:</p>
<ul>
<li>Every element in <code>left</code> is less than or equal to every element in <code>right</code>.</li>
<li><code>left</code> and <code>right</code> are non-empty.</li>
<li><code>left</code> has the smallest possible size.</li>
</ul>
<p>Return the <strong>length</strong> of <code>left</code> after such a partitioning.  It is guaranteed that such a partitioning exists.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>nums = <span id="example-input-1-1">[5,0,3,8,6]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>left = [5,0,3], right = [8,6]
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>nums = <span id="example-input-2-1">[1,1,1,0,6,12]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>left = [1,1,1,0], right = [6,12]
</pre>
<p> </p>

<p><strong>Note:</strong></p>
<ol>
<li><code>2 &lt;= nums.length &lt;= 30000</code></li>
<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
<li>It is guaranteed there is at least one way to partition <code>nums</code> as described.</li>
</ol>

 



If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/partition-array-into-disjoint-intervals
[me]: https://github.com/bumblebee211196/awesome-python-leetcode