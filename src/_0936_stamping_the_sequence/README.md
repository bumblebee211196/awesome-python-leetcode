# [936. Stamping The Sequence][title]

<p>You want to form a <code>target</code> string of <strong>lowercase letters</strong>.</p>
<p>At the beginning, your sequence is <code>target.length</code> <code>'?'</code> marks.  You also have a <code>stamp</code> of lowercase letters.</p>
<p>On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to <code>10 * target.length</code> turns.</p>
<p>For example, if the initial sequence is <font face="monospace">"?????"</font>, and your stamp is <code>"abc"</code>,  then you may make <font face="monospace">"abc??", "?abc?", "??abc" </font>in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)</p>
<p>If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.</p>
<p>For example, if the sequence is <font face="monospace">"ababc"</font>, and the stamp is <code>"abc"</code>, then we could return the answer <code>[0, 2]</code>, corresponding to the moves <font face="monospace">"?????" -&gt; "abc??" -&gt; "ababc"</font>.</p>
<p>Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within <code>10 * target.length</code> moves.  Any answers specifying more than this number of moves will not be accepted.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>stamp = <span id="example-input-1-1">"abc"</span>, target = <span id="example-input-1-2">"ababc"</span>
<strong>Output: </strong><span id="example-output-1">[0,2]</span>
([1,0,2] would also be accepted as an answer, as well as some other answers.)
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>stamp = <span id="example-input-2-1">"</span><span id="example-input-2-2">abca</span><span>"</span>, target = <span id="example-input-2-2">"</span><span>aabcaca"</span>
<strong>Output: </strong><span id="example-output-2">[3,0,1]</span>
</pre>

<p> </p>
<p><strong>Note:</strong></p>


<ol>
<li><code>1 &lt;= stamp.length &lt;= target.length &lt;= 1000</code></li>
<li><code>stamp</code> and <code>target</code> only contain lowercase letters.</li>
</ol>

If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/stamping-the-sequence
[me]: https://github.com/bumblebee211196/awesome-python-leetcode