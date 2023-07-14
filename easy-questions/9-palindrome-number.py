# DESCRIPTION
"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


# PLAN
"""
Initial:
    - The problem can be solved with O(n) if you make it a string then compare
      a the index of it from the left and the index from the right to have
      the same letter

Optimised:
    - Shockingly the optimised way is rather simple, I assume it's because 
      builtin functions of Python are written in C so it's a lot faster
      inherently even if code may be less optimised

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
            self, x: int
        ) -> bool:
        # INITIATION
        string_x    = str(x)
        length_x    = len(string_x)
        even_length = (length_x % 2 == 0)

        # GUARD CLAUSES
        # Negative Check
        if x < 0:                                                                   #   # Negatives are inherently False
            return False
        
        # Empty or Single Digit Check
        if (length_x == 0) or (length_x == 1):                                      #   # 0 or 1 digits are inherently True
            return True

        # Spare the Loop if Short
        if (length_x == 2) or (length_x == 3):                                      #   # Saves some time if it's only one number
            if string_x[0] != string_x[-1]:
                return False
            else:
                return True

        # FUNCTION PROPER
        # Get Midpoint
        if even_length:
            array_end = int(length_x >> 1)
        else:
            array_end = int(length_x >> 1) -1
        
        # Letter Checking
        for index in range(array_end):
            if string_x[index] != string_x[-index - 1]:
                return False
        
        # Default Case
        return True



    def optimised_question(
            self, x: int
        ) -> bool:
        return str(x)[::-1] == str(x)




# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

