# [420. Strong Password Checker][title]

<p>A password is considered strong if the below conditions are all met:</p>
<ul>
<li>It has at least <code>6</code> characters and at most <code>20</code> characters.</li>
<li>It contains at least <strong>one lowercase</strong> letter, at least <strong>one uppercase</strong> letter, and at least <strong>one digit</strong>.</li>
<li>It does not contain three repeating characters in a row (i.e., <code>"...aaa..."</code> is weak, but <code>"...aa...a..."</code> is strong, assuming other conditions are met).</li>
</ul>
<p>Given a string <code>password</code>, return <em>the minimum number of steps required to make <code>password</code> strong. if <code>password</code> is already strong, return <code>0</code>.</em></p>
<p>In one step, you can:</p>
<ul>
<li>Insert one character to <code>password</code>,</li>
<li>Delete one character from <code>password</code>, or</li>
<li>Replace one character of <code>password</code> with another character.</li>
</ul>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> password = "a"
<strong>Output:</strong> 5
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> password = "aA1"
<strong>Output:</strong> 3
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> password = "1337C0d3"
<strong>Output:</strong> 0
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= password.length &lt;= 50</code></li>
<li><code>password</code> consists of letters, digits, dot <code>'.'</code> or exclamation mark <code>'!'</code>.</li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/strong-password-checker
[me]: https://github.com/bumblebee211196/awesome-python-leetcode