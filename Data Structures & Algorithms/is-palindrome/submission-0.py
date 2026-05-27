class Solution:
    def isPalindrome(self, s: str) -> bool:
        # New string
        copy = ""

        # Loop through the string
        for c in s:
            # Check if the character is alphanumeric (has only characters & numbers)
            if c.isalnum():
                # Add it to the string
                copy += c.lower()
        # Return true if the string is a reverse of the copy
        return copy == copy[::-1]
        
        