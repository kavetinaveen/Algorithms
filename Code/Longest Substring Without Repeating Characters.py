# Length of the Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1: # If string lenght is 1 then return 1
            return 1
        max_len = 0 # Initialize maximum length
        start = end = 0 # Initialize start and end pointers
        visited = {} # Initialize visited dictionary
        output = '' # Initialize output string
        while end < len(s): # Loop till end pointer reaches end of the string
            curchar = s[end] 
            if curchar in visited: # If current character is in the visited dictionary, change start pointer to max(visited[curchar]+1, start)
                start = max(visited[curchar]+1, start)
            if max_len < end-start+1: # If Updated max length if the new string length is larger
                max_len = end-start+1
            visited[curchar] = end # Update visited dictionary
            end += 1 # Increase end by 1
        return max_len