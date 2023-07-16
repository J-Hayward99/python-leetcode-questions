# DESCRIPTION
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.


"""


# PLAN
"""
Initial:
    - using a quasi pointer
        - list -> set (removes dups)
        - sort list (fixes the way negatives are saved)
    - return the length of the list

"""

from typing import List

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
    def initial_question(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))                                                 #   # NOTE Python doesn't include pointers, this is the closest one can do
        return len(nums)





# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

