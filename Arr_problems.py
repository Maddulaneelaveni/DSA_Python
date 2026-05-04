# 1. Contains Duplicate

#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
     def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
     

# 2. Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):  # Check lengths: If the lengths of the strings are different, they cannot be anagrams
            return False
        countS = {}  # Create frequency dictionaries
        countT = {}
        for i in range(len(s)): # Loop through strings
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT   # Compare dictionaries
    
# Time Complexity : O(n) :  Because we traverse strings once.
    
# Here, I have used two dictionaries to count the frequency of each character in both strings. If the frequency counts are the same for both strings, then they are anagrams, and we return true. Otherwise, we return false.
#  Here I used Hashinvg instead of other approaches like sorting and nested loops because :
# We need:
# Frequency counting
# Fast lookup
# Efficient comparison
# Dictionary is perfect for this.

