# [318. Maximum Product of Word Lengths][title]

<p>Given a string array <code>words</code>, return <em>the maximum value of</em> <code>length(word[i]) * length(word[j])</code> <em>where the two words do not share common letters</em>. If no such two words exist, return <code>0</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["abcw","baz","foo","bar","xtfn","abcdef"]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The two words can be "abcw", "xtfn".
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["a","ab","abc","d","cd","bcd","abcd"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The two words can be "ab", "cd".
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> words = ["a","aa","aaa","aaaa"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> No such pair of words.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>2 &lt;= words.length &lt;= 1000</code></li>
<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
<li><code>words[i]</code> consists only of lowercase English letters.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/maximum-product-of-word-lengths
[me]: https://github.com/bumblebee211196/awesome-python-leetcode