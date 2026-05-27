from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashmap for mapping the charCount to a list of anagrams
        # Use a default hashmap to store the values as lists
        s = defaultdict(list)
        # Loop through each word in the list
        for word in strs:
            # Make a count for the frequency of each char in the alphabet
            count = [0] * 26        # Add 26 0's to a list. 1 for each char. a ... z
            for char in word:       # Loop through each char in the string
                # Sub the ascii of the current char by the ascii of 'a'
                # Ex. 50 - 50 = 0 or 51 - 50 = 1
                count[ord(char) - ord("a")] += 1
            # Add the list of words to the hashmap.
            # Convert the count key to a tuple since list are not hashable in python
            s[tuple(count)].append(word)
        # Return the list of anagrams in the hashmap
        return list(s.values())
