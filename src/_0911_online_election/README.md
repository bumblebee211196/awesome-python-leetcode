# [911. Online Election][title]

<p>In an election, the <code>i</code>-th vote was cast for <code>persons[i]</code> at time <code>times[i]</code>.</p>
<p>Now, we would like to implement the following query function: <code>TopVotedCandidate.q(int t)</code> will return the number of the person that was leading the election at time <code>t</code>.  </p>
<p>Votes cast at time <code>t</code> will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.</p>
<p> </p>

<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong><span id="example-input-1-1">["TopVotedCandidate","q","q","q","q","q","q"]</span>, <span id="example-input-1-2">[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]</span>
<strong>Output: </strong><span id="example-output-1">[null,0,1,1,0,0,1]</span>
<strong>Explanation: </strong>
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= persons.length = times.length &lt;= 5000</code></li>
<li><code>0 &lt;= persons[i] &lt;= persons.length</code></li>
<li><code>times</code> is a strictly increasing array with all elements in <code>[0, 10^9]</code>.</li>
<li><code>TopVotedCandidate.q</code> is called at most <code>10000</code> times per test case.</li>
<li><code>TopVotedCandidate.q(int t)</code> is always called with <code>t &gt;= times[0]</code>.</li>
</ol>



If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/online-election
[me]: https://github.com/bumblebee211196/awesome-python-leetcode