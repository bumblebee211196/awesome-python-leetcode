# [436. Find Right Interval][title]

<p>You are given an array of <code>intervals</code>, where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> and each <code>start<sub>i</sub></code> is <strong>unique</strong>.</p>
<p>The <strong>r</strong><strong>ight</strong><strong> interval</strong> for an interval <code>i</code> is an interval <code>j</code> such that <code>start<sub>j</sub></code><code> &gt;= end<sub>i</sub></code> and <code>start<sub>j</sub></code> is <strong>minimized</strong>.</p>
<p>Return <em>an array of <strong>right interval</strong> indices for each interval <code>i</code></em>. If no <strong>right interval</strong> exists for interval <code>i</code>, then put <code>-1</code> at index <code>i</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[1,2]]
<strong>Output:</strong> [-1]
<strong>Explanation:</strong> There is only one interval in the collection, so it outputs -1.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[3,4],[2,3],[1,2]]
<strong>Output:</strong> [-1,0,1]
<strong>Explanation:</strong> There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start<sub>0</sub> = 3 is the smallest start that is &gt;= end<sub>1</sub> = 3.
The right interval for [1,2] is [2,3] since start<sub>1</sub> = 2 is the smallest start that is &gt;= end<sub>2</sub> = 2.
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> intervals = [[1,4],[2,3],[3,4]]
<strong>Output:</strong> [-1,2,-1]
<strong>Explanation:</strong> There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start<sub>2</sub> = 3 is the smallest start that is &gt;= end<sub>1</sub> = 3.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= intervals.length &lt;= 2 * 10<sup>4</sup></code></li>
<li><code>intervals[i].length == 2</code></li>
<li><code>-10<sup>6</sup> &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
<li>The start point of each interval is <strong>unique</strong>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/find-right-interval
[me]: https://github.com/bumblebee211196/awesome-python-leetcode