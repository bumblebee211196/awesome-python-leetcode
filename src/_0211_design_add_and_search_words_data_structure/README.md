# [211. Design Add and Search Words Data Structure][title]

<p>Design a data structure that supports adding new words and finding if a string matches any previously added string.</p>
<p>Implement the <code>WordDictionary</code> class:</p>
<ul>
<li><code>WordDictionary()</code> Initializes the object.</li>
<li><code>void addWord(word)</code> Adds <code>word</code> to the data structure, it can be matched later.</li>
<li><code>bool search(word)</code> Returns <code>true</code> if there is any string in the data structure that matches <code>word</code> or <code>false</code> otherwise. <code>word</code> may contain dots <code>'.'</code> where dots can be matched with any letter.</li>
</ul>
<p> </p>
<p><strong>Example:</strong></p>
<pre><strong>Input</strong>
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
<strong>Output</strong>
[null,null,null,null,false,true,true,true]

<strong>Explanation</strong>
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= word.length &lt;= 500</code></li>
<li><code>word</code> in <code>addWord</code> consists lower-case English letters.</li>
<li><code>word</code> in <code>search</code> consist of  <code>'.'</code> or lower-case English letters.</li>
<li>At most <code>50000</code> calls will be made to <code>addWord</code> and <code>search</code>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/design-add-and-search-words-data-structure
[me]: https://github.com/bumblebee211196/awesome-python-leetcode