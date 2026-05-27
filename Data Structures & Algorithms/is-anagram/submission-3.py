from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ Args: 
            s (string): String 1
            t (string): String 2

            Returns:
                bool: True if strings are anagrams
                bool : False if strings are NOT anagrams
        """
        # Check the length of strings
        if len(s) != len(t):
            return False
        
        # Get the counter of each string
        count_s = dict(Counter(s))
        count_t = dict(Counter(t))
        
        if count_s != count_t:
            return False
        else:
            return True

        # Use a hashmap to get the counter of all the letters of each string
        # s_map = {}
        # t_map = {}

        # Loop through each string, adding a counter to each letter
        # for l in s:
