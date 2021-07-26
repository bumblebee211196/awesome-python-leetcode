# [546. Remove Boxes][title]

<p>You are given several <code>boxes</code> with different colors represented by different positive numbers.</p>
<p>You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of <code>k</code> boxes, <code>k &gt;= 1</code>), remove them and get <code>k * k</code> points.</p>
<p>Return <em>the maximum points you can get</em>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> boxes = [1,3,2,2,2,3,4,3,1]
<strong>Output:</strong> 23
<strong>Explanation:</strong>
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----&gt; [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----&gt; [1, 3, 3, 3, 1] (1*1=1 points) 
----&gt; [1, 1] (3*3=9 points) 
----&gt; [] (2*2=4 points)
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> boxes = [1,1,1]
<strong>Output:</strong> 9
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> boxes = [1]
<strong>Output:</strong> 1
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= boxes.length &lt;= 100</code></li>
<li><code>1 &lt;= boxes[i] &lt;= 100</code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/remove-boxes
[me]: https://github.com/bumblebee211196/awesome-python-leetcode