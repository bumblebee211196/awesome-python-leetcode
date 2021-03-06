# [945. Minimum Increment to Make Array Unique][title]

<p>Given an array of integers nums, a <em>move</em> consists of choosing any <code>nums[i]</code>, and incrementing it by <code>1</code>.</p>
<p>Return the least number of moves to make every value in <code>nums</code> unique.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>nums = <span id="example-input-1-1">[1,2,2]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong> After 1 move, the array could be [1, 2, 3].
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>nums = <span id="example-input-2-1">[3,2,1,2,1,7]</span>
<strong>Output: </strong><span id="example-output-2">6</span>
<strong>Explanation: </strong> After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
</pre>
<p> </p>

<p><strong>Note:</strong></p>
<ol>
<li><code>0 &lt;= nums.length &lt;= 40000</code></li>
<li><code>0 &lt;= nums[i] &lt; 40000</code></li>
</ol>

 



If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/minimum-increment-to-make-array-unique
[me]: https://github.com/bumblebee211196/awesome-python-leetcode