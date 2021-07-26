# [963. Minimum Area Rectangle II][title]

<p>Given a set of points in the xy-plane, determine the minimum area of <strong>any</strong> rectangle formed from these points, with sides <strong>not necessarily parallel</strong> to the x and y axes.</p>
<p>If there isn't any rectangle, return 0.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/21/1a.png" style="width: 150px; height: 151px;"/></p>
<pre><strong>Input: </strong><span id="example-input-1-1">[[1,2],[2,1],[1,0],[0,1]]</span>
<strong>Output: </strong><span id="example-output-1">2.00000
<strong>Explanation:</strong> </span><span>The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.</span>
</pre>

<p><strong>Example 2:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/22/2.png" style="width: 150px; height: 94px;"/></p>
<pre><strong>Input: </strong><span id="example-input-2-1">[[0,1],[2,1],[1,1],[1,0],[2,0]]</span>
<strong>Output: </strong><span id="example-output-2">1.00000
</span><strong>Explanation:</strong> The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
</pre>

<p><strong>Example 3:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/22/3.png" style="width: 160px; height: 167px;"/></p>
<pre><strong>Input: </strong><span id="example-input-3-1">[[0,3],[1,2],[3,1],[1,3],[2,1]]</span>
<strong>Output: </strong><span id="example-output-3">0
</span><span><strong>Explanation:</strong> There is no possible rectangle to form from these points.</span>
</pre>

<p><strong>Example 4:</strong></p>
<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/21/4c.png" style="width: 160px; height: 155px;"/></p>
<pre><strong>Input: </strong><span id="example-input-4-1">[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]</span>
<strong>Output: </strong><span id="example-output-4">2.00000
</span><span><strong>Explanation:</strong> The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.</span>
</pre>

<p> </p>


<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= points.length &lt;= 50</code></li>
<li><code>0 &lt;= points[i][0] &lt;= 40000</code></li>
<li><code>0 &lt;= points[i][1] &lt;= 40000</code></li>
<li>All points are distinct.</li>
<li>Answers within <code>10^-5</code> of the actual value will be accepted as correct.</li>
</ol>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/minimum-area-rectangle-ii
[me]: https://github.com/bumblebee211196/awesome-python-leetcode