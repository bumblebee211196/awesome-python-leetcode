# [375. Guess Number Higher or Lower II][title]

<p>We are playing the Guessing Game. The game will work as follows:</p>
<ol>
<li>I pick a number between <code>1</code> and <code>n</code>.</li>
<li>You guess a number.</li>
<li>If you guess the right number, <strong>you win the game</strong>.</li>
<li>If you guess the wrong number, then I will tell you whether the number I picked is <strong>higher or lower</strong>, and you will continue guessing.</li>
<li>Every time you guess a wrong number <code>x</code>, you will pay <code>x</code> dollars. If you run out of money, <strong>you lose the game</strong>.</li>
</ol>
<p>Given a particular <code>n</code>, return <em>the minimum amount of money you need to <strong>guarantee a win regardless of what number I pick</strong></em>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/graph.png" style="width: 505px; height: 388px;"/>
<pre><strong>Input:</strong> n = 10
<strong>Output:</strong> 16
<strong>Explanation:</strong> The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is only one possible number, so you can guess 1 and not have to pay anything.
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= n &lt;= 200</code></li>
</ul>


If you love Data Structures and Algorithms in Python, give this [repo][me] a star :wink:

[title]: https://leetcode.com/problems/guess-number-higher-or-lower-ii
[me]: https://github.com/bumblebee211196/awesome-python-leetcode