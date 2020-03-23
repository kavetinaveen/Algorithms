class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip() # Strip white spaces
        if len(str) == 0: # If length of string is 0 then return 0
            return 0
        x = 0 # Initialize string index
        result = 0 # Initialize result value
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # Initialize digits
        sign = 1 # Assign sign 1
        if str[0] == '-': # If first character is - then assign -1 to sign and remove it from string
            sign = -1
            str = str[1:]
        elif str[0] == '+': # If first character is + then assign 1 to sign and remove it from string
            sign = 1
            str = str[1:]
        if len(str) == 0: # Check string length again, if it is 0 return 0
            return 0
        if str[0] not in digits: # If first character not in digits then return 0
            return 0
        while x < len(str): # Iterate through string till the end of the string or non-digit character
            if str[x].isdigit(): # If character is a digit then add it to the result
                result = result*10 + int(str[x])
            else:
                break
            x += 1
        result = sign * result # Multiple result with sign
        if result < -2**31: # If result out of 32 bit limits then return bounds
            return -2**31
        elif result > 2**31-1:
            return 2**31 - 1
        else:
            return result