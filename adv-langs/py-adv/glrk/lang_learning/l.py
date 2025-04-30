"""
Problem: Longest Substring Without Repeating Characters
Description:
Given a string s, find the length of the longest substring without repeating characters.

Requirements:

Implement a function length_of_longest_substring(s: str) -> int.

The function should return the length (an integer) of the longest substring without repeating characters.

The solution should be efficient (ideally O(n) time).

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""

def length_of_longest_substring(s: str) -> int:
    d = {}
    
    # loop 
    for i in range(len(s)):
        if i < len(s)-1 and s[i] == s[i+1]:
            continue                        
        for j in range(i+1, len(s)+1):
            if j < len(s) and s[j] == s[i+1]:
                continue         
            sub_string = s[i:j]            
            if sub_string not in d:
                d.setdefault(sub_string, 0)
            else:
                d[sub_string] += 1
                
    return d                
                
t = "abcabcbb"
print(length_of_longest_substring(t))   