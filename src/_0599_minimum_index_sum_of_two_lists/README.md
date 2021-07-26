# [599. Minimum Index Sum of Two Lists][title]

<p>Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.</p>
<p>You need to help them find out their <b>common interest</b> with the <b>least list index sum</b>. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
<strong>Output:</strong> ["Shogun"]
<strong>Explanation:</strong> The only restaurant they both like is "Shogun".
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
<strong>Output:</strong> ["Shogun"]
<strong>Explanation:</strong> The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
<strong>Output:</strong> ["KFC","Burger King","Tapioca Express","Shogun"]
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
<strong>Output:</strong> ["KFC","Burger King","Tapioca Express","Shogun"]
</pre>
<p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> list1 = ["KFC"], list2 = ["KFC"]
<strong>Output:</strong> ["KFC"]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= list1.length, list2.length &lt;= 1000</code></li>
<li><code>1 &lt;= list1[i].length, list2[i].length &lt;= 30</code></li>
<li><code>list1[i]</code> and <code>list2[i]</code> consist of spaces <code>' '</code> and English letters.</li>
<li>All the stings of <code>list1</code> are <strong>unique</strong>.</li>
<li>All the stings of <code>list2</code> are <strong>unique</strong>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/minimum-index-sum-of-two-lists
[me]: https://github.com/bumblebee211196/awesome-python-leetcode