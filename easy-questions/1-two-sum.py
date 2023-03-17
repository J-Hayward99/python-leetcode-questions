# DESCRIPTION
"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

"""



# PLAN
"""
Initial solution:
    - Create a loop
    - Get the other number via (target - current number)
    - Look for that

"""

# IMPORTS
from typing import List



# MAIN PIPELINE
def main_pipeline():                                                                # This is the main pipeline of what the code runs
    check_pipeline()                                                                #   # This is used to check, leave as pass if not needed
    question_solution = Solution()
    

    # INITIAL QUESTION
    print("--- Initial Answer ---")
    print(question_solution.initial_question(nums=[2,7,11,15],      target=9))      #   # First example test
    print(question_solution.initial_question(nums=[3,2,4],          target=6))      #   # Second example test
    print(question_solution.initial_question(nums=[3,3],            target=6))      #   # Third example test


    # optimised QUESTION
    print("\n--- Optimised Answer ---")
    print(question_solution.optimised_question(nums=[2,7,11,15],    target=9))      #   # First example test
    print(question_solution.optimised_question(nums=[3,2,4],        target=6))      #   # Second example test
    print(question_solution.optimised_question(nums=[3,3],          target=6))      #   # Third example test


def check_pipeline():                                                               # This is the pipeline that runs checks if required
    pass



# CLASSES
class Solution:                                                                     # Class of the solution
    def initial_question(self, nums: List[int], target: int) -> List[int]:          # Function of the question
        # INITIATION
        nums_length = len(nums)                                                     #   # Quality of Life variable

        # SEARCHING
        for first_index in range(nums_length):                                      #   # Index for the first number
            for second_index in range((first_index + 1), nums_length):              #   # Index for the second number
                # Other Number
                other_number = target - nums[first_index]                           #   # What the second number should be given the first

                # Comparison        
                if nums[second_index] == other_number:                              #   # If the second number is found
                    return [first_index, second_index]
                

    def optimised_question(self, nums: List[int], target: int) -> List[int]:        # This is the optimised answer using hashmaps(dicts)
        """
            This is the optimised method that reduces the time from O(n^2)
            to O(n). 
            
            This is done by turning the double for-loop into a single
            for-loop that utilises a hashmap (dictionary), that has O(1) 
            searching, thus making the overall efficiency O(n)

            For clarity, this solution will progressively build the hashmap
            then check it when it receives another number from the iteration.
            This is different to the initial solution as that one searches for
            the next number (investigate) instead of looking back at previously
            passed numbers (review)

        """
        # INITIATION
        hashmap_nums    = {}                                                        #   # Empty dict
        nums_range      = range(len(nums))                                          #   # Quality of Life variable
        
        # COMPARISON
        for index in nums_range:                                                    #   # Iterate for all the numbers
            # SECOND NUMBER
            other_number = target - nums[index]                                     #   # What the second number should be given the first
            
            if other_number in hashmap_nums:                                        #   # Check if the number is in the hashmap
                return [hashmap_nums[other_number], index]                          #   # If so, return it
            
            hashmap_nums[nums[index]] = index                                       #   # (Else) add the number to the hashmap and iterate

            



# MAIN
main_pipeline()                                                                     # Runs the main pipeline


