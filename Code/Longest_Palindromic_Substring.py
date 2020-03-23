# Longest Palindromic Substring. Assuming string's maximum length is 1000.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) # Length of the input string
        if n <= 1: # If the length of the string is 1 then return input string
            return s
        longest_len = 0 # Initialize longest palindromic substring length
        left = 0 # Initialize the starting point of the palindromic substring
        DP = [[False]*n for x in range(n)] # Initialize DP solutions
        for j in range(n): # Run through the DP solution upper triangular matrix 
            for i in range(j+1):
                if i == j: # If i == j then assign DP to True, single character is always palindromic substring
                    DP[i][j] = True
                elif i+1 == j: # If if i + 1 == j then assign DP to true, if two consecutive characters are same then it is a palindromic substring
                    DP[i][j] = s[i] == s[j]
                elif DP[i+1][j-1] and s[i] == s[j]: # A string Si .... Sj is palindromic substring if Si+1 .... Sj-1 is palindromic and Si == Sj
                    DP[i][j] = True
                if DP[i][j] and longest_len < j - i + 1: # If Si .... Sj is palindromic substring and longest_len < j - i + 1 then update longest_len = j - i + 1 and starting point to i
                    longest_len = j - i + 1
                    left = i
        return s[left:(left+longest_len)]