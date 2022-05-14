# [LeetCode](https://leetcode.com/problemset/all/) study plan

![Language](https://img.shields.io/badge/language-Python-orange.svg)&nbsp;
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)&nbsp;
![Progress](https://img.shields.io/badge/progress-117%20%2F%202234-ff69b4.svg)&nbsp;
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=edab.leetcode.studyplan)

My solution for LeetCode problems using Python.

## Topics

- Techniques
  - [Bit Manipulation](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#bit-manipulation)
  - [Two Pointers](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#two-pointers)
- Programming paradigms
  - [BackTracking](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#backtracking)
  - [Dynamic Programming](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#dynamic-programming)
  - [Greedy](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#greedy)
  = [Memoization](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#memoization)
- Data Structures
  - [Array](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#array)
  - [Binary Heap](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#binary-heap)
  - [Graph](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#graph)
  - [Hash Table](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#hash-table)
  - [Linked List](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#linked-list)
  - [Queue](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#array)
  - [Stack](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#stack)
  - [String](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#string)
  - [Tree](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#tree)
- Algorithms
  - [Binary Search](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#binary-search)
  - [Design](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#design)
  - [Sorting](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#sorting)
  - [Path planning](https://github.com/edab/LC_StudyPlan_Python/blob/main/README.md#path-planning)

## Techniques

### Bit Manipulation

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|  136 | [Single Number](solutions/single-number.py) | Easy | . | . |
|  190 | [Reverse Bits](solutions/reverse-bits.py) | Easy | . | . |
|  191 | [Number of 1 Bits](solutions/number-of-1-bits.py) | Easy | . | . |
|  231 | [Power of Two](solutions/power-of-two.py)| Easy | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Two Pointers

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   11 | [Container With Most Water](solutions/container-with-most-water.py) | Medium | O(n) | O(1) | TwoPointers
|   15 | [3Sum](solutions/3sum.py) | Medium | O(n) | O(1) | TwoPointers
|  125 | [Valid Palindrome](solutions/valid-palindrome.py) | Easy | O(n) | O(1) | TwoPointers
|  167 | [Two Sum II - Input array is sorted](solutions/two-sum-ii-input-array-is-sorted.py)| Medium | O(n) | O(1) | HashMap, TwoPointers
|  283 | [Move Zeroes](solutions/move-zeroes.py) | Easy | O(n) | O(1) | TwoPointers
|  344 | [Reverse String](solutions/reverse-string.py) | Easy | O(n) | O(1) | TwoPointers
|  581 | [Shortest Unsorted Continuous Subarray](solutions/shortest-unsorted-continuous-subarray.py) | Medium | O(n) | O(1) | TwoPointers
|  844 | [Backspace String Compare](solutions/backspace-string-compare.py) | Easy | O(n) | O(1) | TwoPointer backwards
|  905 | [Sort Array By Parity](solutions/sort-array-by-parity.py) | Easy | O(n) | O(1)
|  977 | [Squares of a Sorted Array](solutions/squares-of-a-sorted-array.py) | Easy | O(n) | O(1) | TwoPointers

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

## Programming paradigms

### Backtracking

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   17 | [Letter Combinations of a Phone Number](solutions/letter-combinations-of-a-phone-number.py) | Medium | O(n * 4^n) | O(1) | Backtraking
|   22 | [Generate Parentheses](solutions/generate-parentheses.py) | Medium | O(2^(n+1)) | O(n) | Backtraking
|   39 | [Combination Sum](solutions/combination-sum.py) | Medium | O(2^t) | O(1) | DFS
|   46 | [Permutations](solutions/permutations.py) | Medium | . | . |
|   47 | [Permutations II](solutions/permutations-ii.py) | Medium | O(n * 2^n) | O(n) | DFS
|   77 | [Combinations](solutions/combinations.py) | Medium | . | . |
|   79 | [Word Search](solutions/word-search.py) | Medium | . | . |
|  216 | [Combination Sum III](solutions/combination-sum-iii.py) | Medium | O(k * C(n, k)) | O(k) | DFS
|  784 | [Letter Case Permutation](solutions/letter-case-permutation.py) | Medium | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Dynamic Programming

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   70 | [Climbing Stairs](solutions/climbing-stairs.py) | Easy | . | . |
|  120 | [Triangle](solutions/triangle.py) | Medium | . | . |
|  198 | [House Robber](solutions/house-robber.py) | Medium | . | . |
|  303 | [Range Sum Query - Immutable](solutions/range-sum-query-immutable.py) | Easy | . | . |
|  307 | [Range Sum Query - Mutable](solutions/range-sum-query-mutable.py) | Medium | . | . |
|  322 | [Coin Change](solutions/coin-change.py) | Medium | O(m * n) | O(m) |
| 1641 | [](solutions/count-sorted-vowel-strings.py) | Medium | O(n) | O(1) |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Greedy

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   42 | [Trapping Rain Water](solutions/trapping-rain-water.py) | Hard | . | . |
|   55 | [Jump Game](solutions/jump-game.py) | Medium | . | . |
|  134 | [Gas Station](solutions/gas-station.py) | Medium | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Memoization

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|  518 | [Coin Change 2](solutions/coin-change-2.py) | Medium | O(m * n) | O(m * n) | DFS

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

## Data Structures

### Array

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   26 | [Remove Duplicates from Sorted Array](solutions/remove-duplicates-from-sorted-array.py) | Easy | . | . |
|  121 | [Best Time to Buy and Sell Stock](solutions/best-time-to-buy-and-sell-stock.py) | Easy | . | . | SlidingWindow
|  128 | [Longest Consecutive Sequence](solutions/longest-consecutive-sequence.py) | O(α(n)) | O(n) | DSU, HashSet, HashMap
|  169 | [Majority Element](solutions/majority-element.py) | Easy | . | . |
|  189 | [Rotate Array](solutions/rotate-array.py) | Medium | . | . |
|  215 | [Kth Largest Element in an Array](solutions/kth-largest-element-in-an-array.py) | Medium | . | . |
| 238* | [Product of Array Except Self](solutions/product-of-array-except-self.py) | Medium | O(n) | O(1) |
|  424 | [Longest Repeating Character Replacement](solutions/longest-repeating-character-replacement.py) | Medium | O(n) | O(1) | SlidingWindow
|  704 | [Binary Search](solutions/binary-search.py)| Easy | . | . |
|  807 | [Max Increase to Keep City Skyline](solutions/max-increase-to-keep-city-skyline.py) | Medium | . | . |
| 1337 | [The K Weakest Rows in a Matrix](solutions/the-k-weakest-rows-in-a-matrix.py) | Easy | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Binary Heap

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|  347 | [Top K Frequent Elements](solutions/top-k-frequent-elements.py) | Medium | O(n) | O(n) |
|  621 | [Task Scheduler](solutions/task-scheduler.py) | Medium | O(n) | O(1) |
|  703 | [Kth Largest Element in a Stream](solutions/kth-largest-element-in-a-stream.py) | Easy | . | . |
| 1046 | [Last Stone Weight](solutions/last-stone-weight.py) | Easy | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Graph

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|  133 | [Clone Graph](solutions/clone-graph.py) | Medium | . | . | DFS
|  200 | [Number of Island](solutions/number-of-islands.py) | Medium | . | . | DFS, BFS
|  207 | [Course Schedule](solutions/course-schedule.py) | Medium | . | . | DFS cycle
|  210 | [Course Schedule II](solutions/course-schedule-ii.py) | Medium | . | . |
|  417 | [Pacific Atlantic Water Flow](solutions/pacific-atlantic-water-flow.py) | Medium | . | . | DFS and Sets
|  542 | [01 Matrix](solutions/01-matrix.py) | Medium | . | . | BFS, DP
|  547 | [Number of Provinces](solutions/number-of-provinces.py) | Medium | . | . | DFS
|  695 | [Max Area of Island](solutions/max-area-of-island.py) | Medium | . | . |
|  733 | [Flood Fill](solutions/flood-fill.py) | Easy | . | . |
|  797 | [All Paths From Source to Target](solutions/all-paths-from-source-to-target.py) | Medium | . | . |
|  841 | [Keys and Rooms](solutions/keys-and-rooms.py) | Medium | . | . |
|  934 | [Shortest Bridge](solutions/shortest-bridge.py) | Medium | . | . | BFS multi source and DFS
|  994 | [Rotting Oranges](solutions/rotting-oranges.py) | Medium | . | . | BFS multi source
|  997 | [Find the Town Judge](solutions/find-the-town-judge.py) | Easy | . | . |
| 1020 | [Number of Enclaves](solutions/number-of-enclaves.py) | Medium | . | . | DFS
| 1091 | [Shortest Path in Binary Matrix](solutions/shortest-path-in-binary-matrix.py) | Medium | . | . | BFS
| 1162 | [As Far from Land as Possible](solutions/as-far-from-land-as-possible.py) | Medium | . | . | BFS multi source
| 1254 | [Number of Closed Islands](solutions/number-of-closed-islands.py) | Medium | . | . | DFS 2 pass
| 1319 | [Number of Operations to Make Network Connected](solutions/number-of-operations-to-make-network-connected.py) | Medium | . | . | DFS
| 1791 | [Find Center of Star Graph](solutions/find-center-of-star-graph.py) | Easy | . | . |
| 1905 | [Count Sub Islands](solutions/count-sub-islands.py) | Medium | . | . |
| 1926 | [Nearest Exit from Entrance in Maze](solutions/nearest-exit-from-entrance-in-maze.py) | Medium  | . | . |
| 1971 | [Find if Path Exists in Graph](solutions/find-if-path-exists-in-graph.py) | Easy | . | . | DFS_(i, r) and BFS_(i, r)

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Hash Table

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|    1 | [Two Sum](solutions/two-sum.py) | Easy | O(n) | O(n) |
|   13 | [Roman to Integer](solutions/roman-to-integer.py) | Easy | . | . |
|   36 | [Valid Sudoku](solutions/valid-sudoku.py) | Medium | . | . |
|   49 | [Group Anagrams](solutions/group-anagrams.py) | Medium | O(n*m) | O(n*m) |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Linked List

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|    2 | [Add Two Numbers](solutions/add-two-numbers.py) | Medium | . | . |
|   19 | [Remove Nth Node From End of List](solutions/remove-nth-node-from-end-of-list.py) | Medium | . | . | Two Pointers
|   21 | [Merge Two Sorted Lists](solutions/merge-two-sorted-lists.py) | Easy | . | . |
|  138 | [Copy List with Random Pointer](solutions/copy-list-with-random-pointer.py) | Medium | . | . |
|  141 | [Linked List Cycle](solutions/linked-list-cycle.py) | Easy | . | . |
|  143 | [Reorder List](solutions/reorder-list.py) | Medium | O(n) | O(1) |
|  160 | [Intersection of Two Linked Lists](solutions/intersection-of-two-linked-lists.py) | Easy | . | . |
|  876 | [Middle of the Linked List](solutions/middle-of-the-linked-list.py) | Easy | . | . | Two Pointers

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Queue

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|  239 | [Sliding Window Maximum](solutions/sliding-window-maximum.py) | Hard | . | . | MaxQueue
|  341 | [Flatten Nested List Iterator](solutions/flatten-nested-list-iterator.py) | Medium | . | . | Recursion
|  950 | [](solutions/reveal-cards-in-increasing-order.py) | Medium | O(n) | O(n)
| 1438 | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](solutions/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.py) | Medium | . | . | MaxQueue

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Stack

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   20 | [Valid Parentheses](solutions/valid-parentheses.py) | Easy | . | . |
|   71 | [Simplify Path](solutions/simplify-path.py) | Medium | . | . |
|   84 | [Largest Rectangle in Histogram](solutions/largest-rectangle-in-histogram.py) | Hard | O(n) | O(1) |
|  150 | [Evaluate Reverse Polish Notation](solutions/evaluate-reverse-polish-notation.py) | Medium | . | . |
|  155 | [Min Stack](solutions/min-stack.py) | Easy | . | . |
|  224 | [Basic Calculator](solutions/basic-calculator.py) | Hard | . | . |
|  225 | [Implement Stack using Queues](solutions/implement-stack-using-queues.py) | Easy | . | . |
|  739 | [Daily Temperatures](solutions/daily-temperatures.py) | Medium | O(n) | O(m) | MinStack

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### String

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|    3 | [Longest Substring Without Repeating Characters](solutions/O(α(N))12-substring-without-repeating-characters.py) | Medium | . | . | Sliding Window
|    5 | [Longest Palindromic Substring](solutions/longest-palindromic-substring.py) | Medium | . | . |
|    8 | [String to Integer (atoi)](solutions/string-to-integer-atoi.py) | Medium | . | . |
|  557 | [Reverse Words in a String III](solutions/reverse-words-in-a-string-iii.py) | Easy | . | . |
|  567 | [Permutation in String](solutions/permutation-in-string.py) | Medium | . | . | Sliding Window
|  771 | [Jewels and Stones](solutions/jewels-and-stones.py) | Easy | . | . |
| 1344 | [Angle Between Hands of a Clock](solutions/angle-between-hands-of-a-clock.py) | Medium | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Tree

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   94 | [Binary Tree Inorder Traversal](solutions/binary-tree-inorder-traversal.py) | Easy | . | . |
|   98 | [Validate Binary Search Tree](solutions/validate-binary-search-tree.py) | Medium | . | . |
|  101 | [Symmetric Tree](solutions/symmetric-tree.py) | Easy | . | . |
|  102 | [Binary Tree Level Order Traversal](solutions/binary-tree-level-order-traversal.py) | Medium | . | . | BFS
|  104 | [Maximum Depth of Binary Tree](solutions/maximum-depth-of-binary-tree.py) | Easy | . | . |
|  105 | [Construct Binary Tree from Preorder and Inorder Traversal](aolutions/construct-binary-tree-from-preorder-and-inorder-traversal.py) | Medium | . | . |
|  116 | [Populating Next Right Pointers in Each Node](solutions/populating-next-right-pointers-in-each-node.py) | Easy | . | . |
|  117 | [Populating Next Right Pointers in Each Node II](solutions/populating-next-right-pointers-in-each-node-ii.py) | Easy | O(n) | O(n) | BFS
|  208 | [Implement Trie (Prefix Tree)](solutions/implement-trie-prefix-tree.py) | Medium | . | . |
|  211 | [Design Add and Search Words Data Structure](solutions/design-add-and-search-words-data-structure.py) | Medium | . | . |
|  212 | [Word Search II](solutions/word-search-ii.py) | Medium | . | . |
|  230 | [](solutions/kth-smallest-element-in-a-bst.py) | Medium | O(n) | O(n) | InOrder
|  236 | [Lowest Common Ancestor of a Binary Tree](solutions/lowest-common-ancestor-of-a-binary-tree.py) | Medium | . | . |
|  617 | [Merge Two Binary Trees](solutions/merge-two-binary-trees.py) | Medium | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

## Algorithms

### Binary Search

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   35 | [Search Insert Position](solutions/search-insert-position.py) | Easy | . | . |
|   74 | [Search a 2D Matrix](solutions/) | Medium | Medium | O(log n) | O(1) |
|  278 | [First Bad Version](solutions/first-bad-version.py) | Easy | . | . |
|  374 | [Guess Number Higher or Lower](solutions/guess-number-higher-or-lower.py) | Easy | O(log n) | O(1) |
|  669 | [Trim a Binary Search Tree](solutions/trim-a-binary-search-tree.py) | Medium | O(n) | O(n) |
|  704 | [Binary Search](solutions/binary-search.py) | Easy | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Design

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
| 146 | [LRU Cache](solutions/lru-cache.py) | Medium | . | . |

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Sorting

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|   56 | [Merge Intervals](solutions/merge-intervals.py) | O(nlogn) | O(1) | Intervals
|   57 | [Insert Interval](solutions/insert-interval.py) | Medium | O(n) | O(1) | Intervals
|   88 | [Merge Sorted Array](solutions/merge-sorted-array.py) | Easy | . | . |
|  435 | [Non-overlapping Intervals](solutions/non-overlapping-intervals.py) | Medium | O(nlogn) | O(1) | Intervals
| 1851 | [Minimum Interval to Include Each Query](solutions/minimum-interval-to-include-each-query.py) | Hard | O(nlogn + qlogq) | O(n) | MinHeap
<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>

### Path planning

|    # | Title | Level | Time | Space | Tags   
| ---: | ----  | :---  | :--- | :---  | :---
|  743 | [Network Delay Time](solutions/network-delay-time.py) | Medium | O(V*logE) | O(E) | Djikstra

<div align="right">
    <b><a href="#topics">Back to Top</a></b>
</div>
