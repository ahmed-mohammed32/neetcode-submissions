from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key (list[tuple] of a counter for each char in the list): Value (list of the words)
        dic = defaultdict(list)
        # Loop through words and assign a number from 0 ... 26 to each word
        for s in strs:
            # Counter for each word
            count = [0] * 26
            # Loop through the letters & assign an ASCII value
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Add the list of numbers as the key and the char as the value
            # ex. [0] = a   [1] = b     [2] = c     ...
            dic[tuple(count)].append(s)
        # Return the values (words) back a list
        return list(dic.values())