# [877. Stone Game][title]

<p>Alex and Lee play a game with piles of stones.  There are an even number of piles <strong>arranged in a row</strong>, and each pile has a positive integer number of stones <code>piles[i]</code>.</p>
<p>The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.</p>
<p>Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.</p>
<p>Assuming Alex and Lee play optimally, return <code>True</code> if and only if Alex wins the game.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> piles = [5,3,4,5]
<strong>Output:</strong> true
<strong>Explanation: </strong>
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>2 &lt;= piles.length &lt;= 500</code></li>
<li><code>piles.length</code> is even.</li>
<li><code>1 &lt;= piles[i] &lt;= 500</code></li>
<li><code>sum(piles)</code> is odd.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/stone-game
[me]: https://github.com/bumblebee211196/awesome-python-leetcode