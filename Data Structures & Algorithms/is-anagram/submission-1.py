class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''First attempt: 1st case worked, 2nd failed
            It would return True the first time it found the same character'''
        # Hashmaps/Dictionary's
        dic_s  = {}
        dic_t = {}
        # Compare the lengths of both strings
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            dic_s[s[i]] = 1 + dic_s.get(s[i], 0)
            dic_t[t[i]] = 1 + dic_t.get(t[i], 0)
        # Compare the keys, return False if not the same
        for j in dic_s:
            if dic_s.get(j) != dic_t.get(j):
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
