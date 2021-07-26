# [813. Largest Sum of Averages][title]

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. You can partition the array into <strong>at most</strong> <code>k</code> non-empty adjacent subarrays. The <strong>score</strong> of a partition is the sum of the averages of each subarray.</p>
<p>Note that the partition must use every integer in <code>nums</code>, and that the score is not necessarily an integer.</p>
<p>Return <em>the maximum <strong>score</strong> you can achieve of all the possible partitions</em>. Answers within <code>10<sup>-6</sup></code> of the actual answer will be accepted.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [9,1,2,3,9], k = 3
<strong>Output:</strong> 20.00000
<strong>Explanation:</strong> 
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,5,6,7], k = 4
<strong>Output:</strong> 20.50000
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= nums.length &lt;= 100</code></li>
<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/largest-sum-of-averages
[me]: https://github.com/bumblebee211196/awesome-python-leetcode