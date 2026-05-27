class Solution:
    def isValid(self, s: str) -> bool:
        # Stack for comparing the popped brackets. Hashmap for checking the bracket if they are in the 
        # order.
        stack = []
        bracket_map = { ')': '(', 
                        ']': '[', 
                        '}': '{'
                     }
        # Loop through the string
        for c in s:
            # Add an open bracket to the stack
            if c not in bracket_map:
                stack.append(c)
            else:
                # If stack is empty, return false
                if not stack:
                    return False
                # Otherwise, pop it from the stack and compare it to the bracket map's key
                popped = stack.pop()
                if popped != bracket_map[c]:
                    return False
        return not stack

        