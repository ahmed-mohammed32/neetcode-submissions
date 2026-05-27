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

        #       1st approach : import Counter
        # --------------------------------------
        
        # # Get the counter of each string
        # count_s = dict(Counter(s))
        # count_t = dict(Counter(t))
        
        # if count_s != count_t:
        #     return False
        # else:
        #     return True


        #       2nd approach : raw hashmaps
        # ------------------------------------

        # Use a hashmap to get the counter of all the letters of each string
        s_map = {}
        t_map = {}

        # Loop through each string, adding a counter to each letter
        for i in range(len(s)):
            
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        # Compare the values
        if s_map != t_map:
            return False
        else:
            return True
