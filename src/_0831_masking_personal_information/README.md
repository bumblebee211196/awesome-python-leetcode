# [831. Masking Personal Information][title]

<p>We are given a personal information string <code>s</code>, which may represent either <strong>an email address</strong> or <strong>a phone number.</strong></p>
<p>We would like to mask this personal information according to the following rules:</p>
<p><br/>
<u><strong>1. Email address:</strong></u></p>
<p>We define a <strong>name</strong> to be a string of <code>length ≥ 2</code> consisting of only lowercase letters <code>a-z</code> or uppercase letters <code>A-Z</code>.</p>
<p>An email address starts with a name, followed by the symbol <code>'@'</code>, followed by a name, followed by the dot <code>'.'</code> and followed by a name. </p>
<p>All email addresses are guaranteed to be valid and in the format of <code>"name1@name2.name3".</code></p>
<p>To mask an email, <strong>all names must be converted to lowercase</strong> and <strong>all letters between the first and last letter of the first name</strong> must be replaced by 5 asterisks <code>'*'</code>.</p>
<p><br/>
<u><strong>2. Phone number:</strong></u></p>
<p>A phone number is a string consisting of only the digits <code>0-9</code> or the characters from the set <code>{'+', '-', '(', ')', ' '}.</code> You may assume a phone number contains 10 to 13 digits.</p>
<p>The last 10 digits make up the local number, while the digits before those make up the country code. Note that the country code is optional. We want to expose only the last 4 digits and mask all other digits.</p>
<p>The local number should be formatted and masked as <code>"***-***-1111", </code>where <code>1</code> represents the exposed digits.</p>
<p>To mask a phone number with country code like <code>"+111 111 111 1111"</code>, we write it in the form <code>"+***-***-***-1111".</code>  The <code>'+'</code> sign and the first <code>'-'</code> sign before the local number should only exist if there is a country code.  For example, a 12 digit phone number mask should start with <code>"+**-"</code>.</p>
<p>Note that extraneous characters like <code>"(", ")", " "</code>, as well as extra dashes or plus signs not part of the above formatting scheme should be removed.</p>
<p> </p>
<p>Return the correct "mask" of the information provided.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>s = "LeetCode@LeetCode.com"
<strong>Output: </strong>"l*****e@leetcode.com"
<strong>Explanation: </strong>All names are converted to lowercase, and the letters between the
             first and last letter of the first name is replaced by 5 asterisks.
             Therefore, "leetcode" -&gt; "l*****e".
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>s = "AB@qq.com"
<strong>Output: </strong>"a*****b@qq.com"
<strong>Explanation: </strong>There must be 5 asterisks between the first and last letter 
             of the first name "ab". Therefore, "ab" -&gt; "a*****b".
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>s = "1(234)567-890"
<strong>Output: </strong>"***-***-7890"
<strong>Explanation:</strong> 10 digits in the phone number, which means all digits make up the local number.
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input: </strong>s = "86-(10)12345678"
<strong>Output: </strong>"+**-***-***-5678"
<strong>Explanation:</strong> 12 digits, 2 digits for country code and 10 digits for local number. 
</pre>
<p><strong>Notes:</strong></p>
<ol>
<li><code>s.length &lt;= 40</code>.</li>
<li>Emails have length at least 8.</li>
<li>Phone numbers have length at least 10.</li>
</ol>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/masking-personal-information
[me]: https://github.com/bumblebee211196/awesome-python-leetcode