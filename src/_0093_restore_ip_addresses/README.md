# [93. Restore IP Addresses][title]

<p>Given a string <code>s</code> containing only digits, return all possible valid IP addresses that can be obtained from <code>s</code>. You can return them in <strong>any</strong> order.</p>
<p>A <strong>valid IP address</strong> consists of exactly four integers, each integer is between <code>0</code> and <code>255</code>, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are <strong>valid</strong> IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are <strong>invalid</strong> IP addresses. </p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "25525511135"
<strong>Output:</strong> ["255.255.11.135","255.255.111.35"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "0000"
<strong>Output:</strong> ["0.0.0.0"]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "1111"
<strong>Output:</strong> ["1.1.1.1"]
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> s = "010010"
<strong>Output:</strong> ["0.10.0.10","0.100.1.0"]
</pre><p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> s = "101023"
<strong>Output:</strong> ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>0 &lt;= s.length &lt;= 3000</code></li>
<li><code>s</code> consists of digits only.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/restore-ip-addresses
[me]: https://github.com/bumblebee211196/awesome-python-leetcode