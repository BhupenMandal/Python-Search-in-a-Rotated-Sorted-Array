# Python-Search-in-a-Rotated-Sorted-Array

## Task Description
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

## Explanation
The provided array is rotated sorted array. For this reason, the amount of shift of the array is found. 
This is the pivot. Then binary search is being implemented in the two divided parts. 

Time Complexity: O(log(n)) where n is the size of the rotated sorted array

Space Complexity: The recursive version of Binary Search has a space complexity of O(log(n)) 