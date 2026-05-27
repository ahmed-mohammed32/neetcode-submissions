from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key (list[tuple] of a counter for each char in the list): Value (list of the words)
        # Use a hashmap to store the counter for each char
        h_map = defaultdict(list)
        # Loop through each string in strs
        for w in strs:
            # Get the counter of each char in a empty array from 0 ... 26
            count = [0] * 26
            # Loop through each char in each word and bump the counter by 1
            for c in w:
                count[ord(c) - ord('a')] += 1
                # Append the word into a list for the hashmaps values
            h_map[tuple(count)].append(w)
        # Return the values (words) as a list
        return list(h_map.values())
        