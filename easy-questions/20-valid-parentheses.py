# DESCRIPTION
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


"""


# REQUIREMENTS
"""
_requirements_

"""


# NOTES
"""
_other notes_

"""


# PLAN
"""
Initial:
    - Make a stack
    - Keep track of both the stack size, and the number of brackets
    - A valid answer should be 0 for both

Optimised:
    - Same but an optimisation that saves time due to using an array as the 
      iterable instead of a string

"""


# IMPORTS


# CONSTANTS



# GLOBAL VARIABLES



# MAIN PIPELINE
def main_pipeline():                                                                # This is the main pipeline of what the code runs
    check_pipeline()                                                                #   # This is used to check, leave as pass if not needed
    question_solution = Solution()
    

    # INITIAL QUESTION
    print("--- Initial Answer ---")
    

    # optimised QUESTION
    print("\n--- Optimised Answer ---")
    

def check_pipeline():                                                               # This is the pipeline that runs checks if required
    pass


# CLASSES 
class Solution:
    def initial_question(
            self, s:str
        ) -> bool:
        # Initiation
        bracket_stack       = [None]
        stack_size          = 0
        bracket_counter     = 0
        closing_pair_map    = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        # Check String
        for char in s:
            # Opening Bracket Condition
            if char in "({[":
                bracket_counter += 1
                stack_size      += 1
                bracket_stack.append(char)
            
            # Closing Bracket Condition
            if char in ")}]":
                bracket_counter -= 1
                
                # Match Last Open Bracket
                if closing_pair_map[char] == bracket_stack[-1]:
                    bracket_stack.pop()
                    stack_size -= 1

        return (stack_size == 0) and (bracket_counter == 0)




    def optimised_question(
            self, s:str
        ) -> bool:
        # Initiation
        bracket_stack       = [None]
        stack_size          = 0
        bracket_counter     = 0
        closing_pair_map    = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        open_brackets       = closing_pair_map.values()
        closing_brackets    = closing_pair_map.keys()

        # Check String
        for char in s:
            # Opening Bracket Condition
            if char in open_brackets:
                bracket_counter += 1
                stack_size      += 1
                bracket_stack.append(char)
            
            # Closing Bracket Condition
            if char in closing_brackets:
                bracket_counter -= 1
                
                # Match Last Open Bracket
                if closing_pair_map[char] == bracket_stack[-1]:
                    bracket_stack.pop()
                    stack_size -= 1

        return (stack_size == 0) and (bracket_counter == 0)





# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

