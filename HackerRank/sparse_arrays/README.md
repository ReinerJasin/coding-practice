# Sparse Arrays

![Status](https://img.shields.io/badge/Status-Solved-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(Qxn)-beige)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(n)-9cf)

## Problem Overview

| Property | Details |
|----------|---------|
| **Last Updated** | 17 October 2025 |
| **Difficulty** | 🟠 Medium |
| **Language** | Python 3.0 |
| **Category** | Data Structures → Arrays → Sparse Arrays |
| **Source** | [HackerRank Problem ↗](https://www.hackerrank.com/challenges/sparse-arrays/problem) |

---

## Problem Description
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

---

## Function Description
Complete the function $matchingStrings$ with the following parameters:
* $string\ stringList[n]$: an array of strings to search
* $string\ queries[q]$: an array of query strings

Returns
* $int[q]$: the results of each query

---

## Examples
**Example 1**  
Input: <br/>
```
stringList = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
```

Output: <br/>
```
[2,1,0]
```

Explanation: <br/>
* 'ab' query appears 2 times in stringList
* 'abc' query appears 1 time in stringList
* 'bc' query appears 0 times in stringList

---

## Constraints
* $1 \leq n \leq 1000$
* $1 \leq q \leq 1000$
* $1 \leq |stringList[i]|,|queries[i]| \leq 20$

---

## My Approach
I utilized the most natural way to solve this problem, which is check each item in `queries` and check every item in the `stringList`. I made a counter to take account how many times that item appear in the list. every time the item appear, we just increment it by 1.

We do this for each item in `queries`, so make sure to reset the counter back to 0 if we want to check new item.

I am confident that this is not the most optimal solution, but this approach is the most intuitive approach that can be easily implemented by any programmers.

---

## Complexity Analysis
* Time Complexity: `O(Q x n)`
* Space Complexity: `O(n)`

---

## Implementation
* Language: Python 3.0
* See `solution.py` in this folder for the complete code.

---

## Performance
* Runtime: **0.0000s** per test
* Memory: **0.03 KB** per test
* HackerRank Score: **25.00** / 25.00

---

<!-- ## Alternate Approaches (Optional)
List other ways you could have solved the problem:
* Brute force vs optimized solution
* Trade-offs in complexity -->

<!-- --- -->

<!-- ## Lessons Learned (Optional)
Key takeaways, mistakes made, or new techniques learned. -->
