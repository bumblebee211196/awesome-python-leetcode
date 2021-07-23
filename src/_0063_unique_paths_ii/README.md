# [63. Unique Paths II][title]

<p>A robot is located at the top-left corner of a <code>m x n</code> grid (marked 'Start' in the diagram below).</p>
<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).</p>
<p>Now consider if some obstacles are added to the grids. How many unique paths would there be?</p>
<p>An obstacle and space is marked as <code>1</code> and <code>0</code> respectively in the grid.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" style="width: 242px; height: 242px;"/>
<pre><strong>Input:</strong> obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
</pre>
<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" style="width: 162px; height: 162px;"/>
<pre><strong>Input:</strong> obstacleGrid = [[0,1],[0,0]]
<strong>Output:</strong> 1
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>m == obstacleGrid.length</code></li>
<li><code>n == obstacleGrid[i].length</code></li>
<li><code>1 &lt;= m, n &lt;= 100</code></li>
<li><code>obstacleGrid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/unique-paths-ii
[me]: https://github.com/bumblebee211196/awesome-python-leetcode