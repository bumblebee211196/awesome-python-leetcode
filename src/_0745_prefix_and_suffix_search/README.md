# [745. Prefix and Suffix Search][title]

<p>Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.</p>
<p>Implement the <code>WordFilter</code> class:</p>
<ul>
<li><code>WordFilter(string[] words)</code> Initializes the object with the <code>words</code> in the dictionary.</li>
<li><code>f(string prefix, string suffix)</code> Returns <em>the index of the word in the dictionary,</em> which has the prefix <code>prefix</code> and the suffix <code>suffix</code>. If there is more than one valid index, return <strong>the largest</strong> of them. If there is no such word in the dictionary, return <code>-1</code>.</li>
</ul>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input</strong>
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
<strong>Output</strong>
[null, 0]

<strong>Explanation</strong>
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= words.length &lt;= 15000</code></li>
<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
<li><code>1 &lt;= prefix.length, suffix.length &lt;= 10</code></li>
<li><code>words[i]</code>, <code>prefix</code> and <code>suffix</code> consist of lower-case English letters only.</li>
<li>At most <code>15000</code> calls will be made to the function <code>f</code>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/prefix-and-suffix-search
[me]: https://github.com/bumblebee211196/awesome-python-leetcode