# Author: jzhao0105
# Longest Palindromic Substring. Optimized for space complexity.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1: # If string length is <= 1 then return string
            return s

        if len(s) == 2: # If string length is 2 then check the characters if same return the string otherwise return first letter
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        res = s[0] # Initialize the result with first letter

        for i in range(len(s)-1): 
            if i > 0 and s[i] == s[i-1]: # If consecutive letters are same then we can skip loop
                continue

            l , r = i - 1 , i + 1 # Initialize left, right indexes from the current centre i
            temp = [s[i]] # Start with ith character

            while r <= len(s) - 1: # If consecutive elements are same then increase the right by one
                if s[i] == s[r]:
                    temp.append(s[r])
                    r += 1
                else:
                    break

            while l >= 0 and r < len(s): # Expand around the centre
                if s[l] == s[r] and r > i: # Check if left and right letters are same
                    temp.insert(0, s[l]) # If same then insert left letter at the start and right letter at the end
                    temp.append(s[r])
                    l -= 1 
                    r += 1      
                else:
                    break

            if len(temp) > len(res): # Update the result if the current result's length is higher
                res = temp

        return ''.join(res)
   
