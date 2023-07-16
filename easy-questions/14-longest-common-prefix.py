from typing import List
# DESCRIPTION
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""




# PLAN
"""
Initial:
    - Get the smallest string to avoid out-of-bounds errors
    - Iterate through the characters of the string
    - Compare each with the other strings at that index
    - Build up a prefix that adds the character if it's in all the strings
    - Return upon failure

Optimised:
    - This appears to be the fastest way

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
    def initial_question(self, strs: List[str]) -> str:
        prefix          = ""

        # MINIMUM REQUIREMENT CHECK
        # Assume First String
        min_string = strs[0]
        
        # Capture and Hold Smallest
        for string in strs:
            if len(string) < len(min_string):
                min_string = string

        # Check String isn't Empty
        if len(min_string) < 1:
            return min_string
        
        # FUNCTION
        for index, char in enumerate(min_string):
            for string in strs:
                # Different Letter Check
                if char != string[index]:
                    return prefix

            # Bookkeeping
            prefix  += char
        
        return prefix


# MAIN
main_pipeline()                                                                     # Runs the main pipeline

