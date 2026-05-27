class Solution:
    def isValid(self, s: str) -> bool:
        # Hashmap of bracket types
        # dic_s = { '(' : ')', 
        #           '{' : '}',
        #           '[' : ']'
        #           }
        # # Loop through the string & check if it matches with each key value pair
        # for i in s:
        #     if dic_s.get(i) in s:
        #         dic_s.pop(i)
    
        # Empty stack and hashmap for bracket storage & checking
        stack = []
        bracket_map = {
                    ')' : '(',
                    '}' : '{',
                    ']' : '['
                    }
        # Loop through string
        for i in s:
            # Check if the char matches hashmap key
            if i in bracket_map:
                # Check if stack match with open bracket. If not, pop it and end loop
                if stack and stack[-1] == bracket_map[i]:
                    stack.pop()
                else:
                    return False
            # Otherwise, add it to the stack
            else:
                stack.append(i)
        return True if not stack else False
            
            



