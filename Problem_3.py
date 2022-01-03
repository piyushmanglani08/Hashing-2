# Time Complexity : O(n) 
# Space Complexity : O(n) 
# Did this code successfully run on Leetcode : yes	
# Any problem you faced while coding this : Followed approach from the class 
#longest palindrome 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)