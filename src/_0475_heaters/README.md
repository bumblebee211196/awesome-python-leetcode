# [475. Heaters][title]

<p>Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.</p>
<p>Every house can be warmed, as long as the house is within the heater's warm radius range. </p>
<p>Given the positions of <code>houses</code> and <code>heaters</code> on a horizontal line, return <em>the minimum radius standard of heaters so that those heaters could cover all houses.</em></p>
<p><strong>Notice</strong> that all the <code>heaters</code> follow your radius standard, and the warm radius will the same.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> houses = [1,2,3], heaters = [2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> houses = [1,2,3,4], heaters = [1,4]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> houses = [1,5], heaters = [2]
<strong>Output:</strong> 3
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= houses.length, heaters.length &lt;= 3 * 10<sup>4</sup></code></li>
<li><code>1 &lt;= houses[i], heaters[i] &lt;= 10<sup>9</sup></code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/heaters
[me]: https://github.com/bumblebee211196/awesome-python-leetcode