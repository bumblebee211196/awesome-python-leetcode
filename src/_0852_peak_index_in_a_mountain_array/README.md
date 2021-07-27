# [852. Peak Index in a Mountain Array][title]

<p>Let's call an array <code>arr</code> a <strong>mountain</strong> if the following properties hold:</p>
<ul>
<li><code>arr.length &gt;= 3</code></li>
<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
<li><code>arr[0] &lt; arr[1] &lt; ... arr[i-1] &lt; arr[i] </code></li>
<li><code>arr[i] &gt; arr[i+1] &gt; ... &gt; arr[arr.length - 1]</code></li>
</ul>
</li>
</ul>
<p>Given an integer array <code>arr</code> that is <strong>guaranteed</strong> to be a mountain, return any <code>i</code> such that <code>arr[0] &lt; arr[1] &lt; ... arr[i - 1] &lt; arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [0,1,0]
<strong>Output:</strong> 1
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [0,2,1,0]
<strong>Output:</strong> 1
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [0,10,5,2]
<strong>Output:</strong> 1
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> arr = [3,4,5,1]
<strong>Output:</strong> 2
</pre><p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> arr = [24,69,100,99,79,78,67,36,26,19]
<strong>Output:</strong> 2
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>3 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
<li><code>0 &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
<li><code>arr</code> is <strong>guaranteed</strong> to be a mountain array.</li>
</ul>
<p> </p>
<strong>Follow up:</strong> Finding the <code>O(n)</code> is straightforward, could you find an <code>O(log(n))</code> solution?

If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/peak-index-in-a-mountain-array
[me]: https://github.com/bumblebee211196/awesome-python-leetcode