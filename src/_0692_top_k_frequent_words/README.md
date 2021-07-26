# [692. Top K Frequent Words][title]

<p>Given a non-empty list of words, return the <i>k</i> most frequent elements.</p>
<p>Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.</p>
<p><b>Example 1:</b><br/>
</p><pre><b>Input:</b> ["i", "love", "leetcode", "i", "love", "coding"], k = 2
<b>Output:</b> ["i", "love"]
<b>Explanation:</b> "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
</pre>
<p></p>
<p><b>Example 2:</b><br/>
</p><pre><b>Input:</b> ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
<b>Output:</b> ["the", "is", "sunny", "day"]
<b>Explanation:</b> "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
</pre>
<p></p>
<p><b>Note:</b><br/>
</p><ol>
<li>You may assume <i>k</i> is always valid, 1 ≤ <i>k</i> ≤ number of unique elements.</li>
<li>Input words contain only lowercase letters.</li>
</ol>
<p></p>
<p><b>Follow up:</b><br/>
</p><ol>
<li>Try to solve it in <i>O</i>(<i>n</i> log <i>k</i>) time and <i>O</i>(<i>n</i>) extra space.</li>
</ol>
<p></p>

If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/top-k-frequent-words
[me]: https://github.com/bumblebee211196/awesome-python-leetcode