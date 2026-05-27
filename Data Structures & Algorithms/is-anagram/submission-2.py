class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base case: Check if the length is the same
        if len(s) != len(t):
            return False
        
        # Hashmaps for char in each string
        dic_s = {}
        dic_t = {}

        # Loop to add a counter to each Hashmap for each char within the strings
        for i in range(len(s)):
            # Add a counter for each char in both Hashmaps
            dic_s[s[i]] = 1 + dic_s.get(s[i], 0)
            dic_t[t[i]] = 1 + dic_t.get(t[i], 0)
            # Compare counters for both strings
        for c in dic_s:
            if dic_s[c] != dic_t.get(c, 0):
                return False
        return True
            

        # 2 loops - 1 for each string
        # Loop through each and check if it's in the other
        # Return True if all characters are in the other's string
        # Return False if not
        # for i in s:
        #     for j in t:
        #         if i in t:
        #             return True
        # return False

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False
