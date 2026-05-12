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
# Space Complexity : O(1) : Maximum 26 characters. So space is constant.
# Here, I have used two dictionaries to count the frequency of each character in both strings. If the frequency counts are the same for both strings, then they are anagrams, and we return true. Otherwise, we return false.
#  Here I used Hashinvg instead of other approaches like sorting and nested loops because :
# We need:
# Frequency counting
# Fast lookup
# Efficient comparison
# Dictionary is perfect for this.


# 3. Two Sum

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# Return the answer with the smaller index first.
# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


# 4.Find the first 2 highest frequency elements in an array
# Array = [1, 7, 0, 4, 3, 2, 3, 7, 0]

from collections import defaultdict
nums = [1, 7, 0, 4, 3, 2, 3, 7, 0]
freq = defaultdict(int)
for n in nums:
    freq[n] += 1
top2 = sorted(freq, key=freq.get, reverse=True)[:2]
print(top2)

# Here, I used default dictionary because it helps us store frequencies easily without checking whether a key already exists.
# Then we create a list called nums containing the numbers.
# After that, freq = defaultdict(int) creates an empty dictionary where every new key automatically starts with value 0
# the loop for n in nums: goes through each number one by one.
# Inside the loop, freq[n] += 1 increases the count of that number. For example, when 7 appears for the first time its count becomes 1, and when it appears again the count becomes 2
# After the loop finishes, the dictionary stores frequencies like {1:1, 7:2, 0:2, 4:1, 3:2, 2:1}.
# sorted(freq) takes only the keys of the dictionary, which are the numbers
# key=freq.get to sort those keys based on their frequency values stored in the dictionary. For example, freq.get(7) returns 2, freq.get(1) returns 1, and so on
# reverse=True is used, sorting happens from highest frequency to lowest frequency.
# The sorted order becomes something like [7, 0, 3, 1, 4, 2] because 7, 0, and 3 have the highest frequency 2
# Finally, [:2] takes only the first two elements from that sorted list, so the output becomes [7, 0].