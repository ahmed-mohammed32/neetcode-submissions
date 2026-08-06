import sys
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack and bracket_map approach
        stack = []
        bracket_map = {')':'(', ']':'[', '}':'{', }

        # Loop through the string
        for char in s:
            # Check if it's an open bracket, add to stack
            if char not in bracket_map:
                stack.append(char)
            else:
                # Check if the stack is empty
                if not stack:
                    return False
                popped = stack.pop()
                # Check if the brackets match 
                if popped != bracket_map[char]:
                    return False
        # Returns true if stack is not empty
        return not stack

    # for line in sys.stdin:
    #     line = line.strip()
    #     if line:
    #         print(is_valid(line))