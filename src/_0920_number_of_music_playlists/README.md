# [920. Number of Music Playlists][title]

<p>Your music player contains <code>n</code> different songs and she wants to listen to <code>goal</code><strong> </strong>(not necessarily different) songs during your trip.  You create a playlist so that:</p>
<ul>
<li>Every song is played at least once</li>
<li>A song can only be played again only if <code>k</code> other songs have been played</li>
</ul>
<p>Return the number of possible playlists.  <strong>As the answer can be very large, return it modulo </strong><code>10<sup>9</sup> + 7</code>.</p>
<p> </p>



<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>n = <span id="example-input-1-1">3</span>, goal = <span id="example-input-1-2">3</span>, k = <span id="example-input-1-3">1</span>
<strong>Output: </strong><span id="example-output-1">6
<strong>Explanation</strong>: </span><span>There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].</span>
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>n = <span id="example-input-2-1">2</span>, goal = <span id="example-input-2-2">3</span>, k = <span id="example-input-2-3">0</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span id="example-output-1"><strong>Explanation</strong>: </span><span>There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]</span>
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>n = <span id="example-input-3-1">2</span>, goal = <span id="example-input-3-2">3</span>, k = <span id="example-input-3-3">1</span>
<strong>Output: </strong><span id="example-output-3">2
<strong>Explanation</strong>: </span><span>There are 2 possible playlists. [1, 2, 1], [2, 1, 2]</span>
</pre>


<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>0 &lt;= k &lt; n &lt;= goal &lt;= 100</code></li>
</ol>





If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/number-of-music-playlists
[me]: https://github.com/bumblebee211196/awesome-python-leetcode