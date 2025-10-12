# Compare the Triplets

![Status](https://img.shields.io/badge/Status-Solved-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-beige)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(n)-9cf)

> README is still under development. This alert will be removed when it is finished.

## Problem Overview

| Property | Details |
|----------|---------|
| **Last Updated** | 12 October 2025 |
| **Difficulty** | 🟢 Easy |
| **Language** | Python 3.0 |
| **Category** | Prepare → Algorithms → Warmup |
| **Source** | [HackerRank Problem ↗](https://www.hackerrank.com/challenges/compare-the-triplets/problem) |

---

## Problem Description
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to calculate their comparison points by comparing each category:
* If a[i] > b[i], then Alice is awarded 1 point.
* If a[i] < b[i], then Bob is awarded 1 point.
* If a[i] = b[i], then neither person receives a point.

---

## Function Description
Complete the function compareTriplets with the following parameter(s):

* int a[3]: Alice's challenge rating
* int b[3]: Bob's challenge rating

Returns

* int[2]: the first element is Alice's score and the second is Bob's score

---

## Examples
**Example 1**  
Input: <br/>
```
5 6 7
3 6 10
```

Output: <br/>
```
1 1
```

Explanation:
* $a = (a[0],a[1],a[2]) = (5, 6, 7)$

* $b = (b[0],b[1],b[2]) = (3, 6, 10)$

Now let's compare each individual score:
* $a[0] > b[0]$, so Alice receives 1 point.

* $a[1] = b[1]$, so nobody receives a point.

* $a[2] < b[2]$, so Bob receives 1 point.

Alice's compraison score is 1, and Bob's comparison score is 1. Thus, we return the array [1, 1]

---

## Constraints
* $1 \leq a[i] \leq 100$
* $1 \leq b[i] \leq 100$

---

## My Approach
Explain the thought process behind your solution:
* Algorithm or data structure used
* Any tricks or optimizations applied

---

## Complexity Analysis
* Time Complexity: O(n) or whatever fits your solution
* Space Complexity: O(1) or whatever fits your solution

---

## Implementation
* Language: Python
* See solution.py in this folder for the complete code.

---

## Performance (Optional)
* Runtime: X ms, beats Y% of submissions
* Memory: Z MB, beats W% of submissions

---

## Alternate Approaches (Optional)
List other ways you could have solved the problem:
* Brute force vs optimized solution
* Trade-offs in complexity

---

## Lessons Learned (Optional)
Key takeaways, mistakes made, or new techniques learned.
