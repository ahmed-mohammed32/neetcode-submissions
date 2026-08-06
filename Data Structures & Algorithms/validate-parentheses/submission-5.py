class Solution:
    def isValid(self, s: str) -> bool:
        # Stack and map approach
        stack = []
        bracket_map = {  '}': '{',  ')': '(',  ']': '[' }

        # Loop through the string
        for bracket in s:
            # Check if the bracket is in the map
            if bracket not in bracket_map:
                # Add to the stack, otherwise pop from the stack
                stack.append(bracket)
            # Check if stack is empty
            else:
                if not stack:
                    return False
                # Pop from the stack
                popped = stack.pop()
            # Compare the popped and bracket map value
                if popped != bracket_map[bracket]:
                    return False
        # True if stack is not empty
        return not stack
                
