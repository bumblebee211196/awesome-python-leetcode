# [676. Implement Magic Dictionary][title]

<p>Design a data structure that is initialized with a list of <strong>different</strong> words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.</p>
<p>Implement the <code>MagicDictionary</code> class:</p>
<ul>
<li><code>MagicDictionary()</code> Initializes the object.</li>
<li><code>void buildDict(String[] dictionary)</code> Sets the data structure with an array of distinct strings <code>dictionary</code>.</li>
<li><code>bool search(String searchWord)</code> Returns <code>true</code> if you can change <strong>exactly one character</strong> in <code>searchWord</code> to match any string in the data structure, otherwise returns <code>false</code>.</li>
</ul>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input</strong>
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
<strong>Output</strong>
[null, null, false, true, false, false]

<strong>Explanation</strong>
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= dictionary.length &lt;= 100</code></li>
<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
<li><code>dictionary[i]</code> consists of only lower-case English letters.</li>
<li>All the strings in <code>dictionary</code> are <strong>distinct</strong>.</li>
<li><code>1 &lt;= searchWord.length &lt;= 100</code></li>
<li><code>searchWord</code> consists of only lower-case English letters.</li>
<li><code>buildDict</code> will be called only once before <code>search</code>.</li>
<li>At most <code>100</code> calls will be made to <code>search</code>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/implement-magic-dictionary
[me]: https://github.com/bumblebee211196/awesome-python-leetcode