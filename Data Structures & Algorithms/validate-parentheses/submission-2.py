class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack and hashmap to compare the brackets
        stack = []
        bracket_map = { ')':'(', '}':'{', ']':'[' }

        # Loop through the string
        for bracket in s:
            # Check if it's in the hashmap
            if bracket not in bracket_map:
                # Add to stack
                stack.append(bracket)
            # Check the stack is empty
            else:
                if not stack:
                    return False
                    # Pop from the stack
                popped = stack.pop()
                # Compare to the bracket value.
                if popped != bracket_map[bracket]:
                    return False
        # True if stack is not empty
        return not stack
