# [705. Design HashSet][title]

<p>Design a HashSet without using any built-in hash table libraries.</p>
<p>Implement <code>MyHashSet</code> class:</p>
<ul>
<li><code>void add(key)</code> Inserts the value <code>key</code> into the HashSet.</li>
<li><code>bool contains(key)</code> Returns whether the value <code>key</code> exists in the HashSet or not.</li>
<li><code>void remove(key)</code> Removes the value <code>key</code> in the HashSet. If <code>key</code> does not exist in the HashSet, do nothing.</li>
</ul>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input</strong>
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
<strong>Output</strong>
[null, null, null, true, false, null, true, null, false]

<strong>Explanation</strong>
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>0 &lt;= key &lt;= 10<sup>6</sup></code></li>
<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>, <code>remove</code>, and <code>contains</code>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/design-hashset
[me]: https://github.com/bumblebee211196/awesome-python-leetcode