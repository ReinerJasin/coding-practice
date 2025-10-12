# Left Rotation

>**Last Updated:** 11 October 2025

![Status](https://img.shields.io/badge/Status-Solved-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)

![Average Time](https://img.shields.io/badge/Avg%20Time-0s-beige)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-9cf)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(n)-9cf)

<!-- [Problem Link - HackerRank ↗](https://www.hackerrank.com/challenges/array-left-rotation/problem) -->

**Categories:** Data Structures > Arrays > Left Rotation

<a href="https://www.hackerrank.com/challenges/array-left-rotation/problem" target="_blank">Problem Link - HackerRank ↗</a>

---

## Description
The Left Rotation problem wants us to shift the items inside a python array to the left by `d` positions. If an item at the left end fall off, it will reappear at the right end.

---

## Examples
**Example 1**  
Input: <br/>
```
d = 2
arr = [1,2,3,4,5]
```

Output: <br/>
```
[3,4,5,1,2]
```

Explanation: <br/>
[1,2,3,4,5] → [2,3,4,5,1] → [3,4,5,1,2]

---

## Constraints
* $1 \leq n \leq 10^5$
* $1 \leq d \leq n$
* $1 \leq a[i] \leq 10^6$

---

## My Approach

#### 1. Loop and Append
My idea is to loop through the array starting from the index `d`, and for each iteration I would append the item into a new array. When we finish the loop to the last item in the array, I will reset the index back to `0` and continue the loop until `d-1`.

With this approach, I am able to pass the test case and submit the solution in HackerRank, but then I notice that one of the constraint is that `d = n` is one possible use case that is not included on HackerRank's test case. And since we're accessing the array by the index, we will notice that using the raw index will trigger the index out of bound error. Therefore, to keep things simple, I simply add modulo of `n` to make sure that the number will not exceed `n`, and having `n=n` would basically means we're not shifting by any value.

#### 2. Python Slicing
This second solution is kind of tricky, and I wouldn't consider this as my solution although it only takes one line to solve this problem.

The way we do this is just by slicing the array into two parts, and concat them starting from the array the begins with items of the index `d`. So instead of rotating it left by `d` times, we just jump straight to `d` and split the array in half before joining them back in the return and putting arr[d] at the very beginning. So I wouldn't take this as a solution, and I will just use the Solution 1 for this submission.

---

## Complexity Analysis
* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

---

## Implementation
* Language: Python 3
* See `solution.py` in this folder for the complete code.

---

## Performance
* Runtime: **0.0000s** per test
* Memory: **0.10 KB** per test
* HackerRank Score: **20.00** / 20.00

---

## Alternate Approaches
These are some alternate approaches to this problem:
* Three-Reverse Technique

---

## Lessons Learned
* Variable representation can be important, especially when it is used as a loop index.
