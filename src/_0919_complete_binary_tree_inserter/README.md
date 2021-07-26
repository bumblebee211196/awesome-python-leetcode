# [919. Complete Binary Tree Inserter][title]

<p>A <em>complete</em> binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.</p>
<p>Write a data structure <code>CBTInserter</code> that is initialized with a complete binary tree and supports the following operations:</p>
<ul>
<li><code>CBTInserter(TreeNode root)</code> initializes the data structure on a given tree with head node <code>root</code>;</li>
<li><code>CBTInserter.insert(int v)</code> will insert a <code>TreeNode</code> into the tree with value <code>node.val = v</code> so that the tree remains complete, <strong>and returns the value of the parent of the inserted <code>TreeNode</code></strong>;</li>
<li><code>CBTInserter.get_root()</code> will return the head node of the tree.</li>
</ul>
<ol>
</ol>

<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>inputs = <span id="example-input-1-1">["CBTInserter","insert","get_root"]</span>, inputs = <span id="example-input-1-2">[[[1]],[2],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,1,[1,2]]</span>
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>inputs = <span id="example-input-2-1">["CBTInserter","insert","insert","get_root"]</span>, inputs = <span id="example-input-2-2">[[[1,2,3,4,5,6]],[7],[8],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,3,4,[1,2,3,4,5,6,7,8]]</span></pre>


<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li>The initial given tree is complete and contains between <code>1</code> and <code>1000</code> nodes.</li>
<li><code>CBTInserter.insert</code> is called at most <code>10000</code> times per test case.</li>
<li>Every value of a given or inserted node is between <code>0</code> and <code>5000</code>.</li>
</ol>



<p> </p>
 



If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/complete-binary-tree-inserter
[me]: https://github.com/bumblebee211196/awesome-python-leetcode