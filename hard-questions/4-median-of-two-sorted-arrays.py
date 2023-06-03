# DESCRIPTION
"""
_summary_

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
_plan_

"""


# IMPORTS
from typing import List


# CONSTANTS



# GLOBAL VARIABLES



# MAIN PIPELINE
def main_pipeline():                                                                # This is the main pipeline of what the code runs
    check_pipeline()                                                                #   # This is used to check, leave as pass if not needed
    question_solution = Solution()
    

    # INITIAL QUESTION
    print("--- Initial Answer ---")
    print(question_solution.initial_question([1,3], [2]))
    print(question_solution.initial_question([1,2], [3, 4]))

    # optimised QUESTION
    print("\n--- Optimised Answer ---")
    # There was no optimised answer for this question

def check_pipeline():                                                               # This is the pipeline that runs checks if required
    pass


# CLASSES 
class Solution:
    def initial_question(self, nums1: List[int], nums2: List[int]) -> float:
        # COMBINED AND SORTED ARRAY
        combined_array          = sorted(nums1 + nums2)                             #   # Creates a sorted array of the two subarrays

        # ACQUIRE VALUES
        length_array            = len(combined_array)
        median_index            = length_array >> 1                                 #   # Bit shift right, halves the value
        truncated_median_index  = median_index >> 0                                 #   # Bit shift right by 0 truncates

        # ODD SIZE ARRAY
        if length_array % 2 == 1:                                                   #   # Determines if the middle is x.5 or x.0, latter rounded up
            return combined_array[truncated_median_index]
        
        # EVEN SIZE ARRAY
        left_number     = combined_array[truncated_median_index - 1]
        right_number    = combined_array[truncated_median_index]
        return (left_number + right_number) * 0.5                                   #   # Multiplied by half, faster than divide by 2





# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

