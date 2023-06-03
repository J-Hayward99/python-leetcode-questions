# DESCRIPTION # FIXME currently doing
"""
Given a string s, find the length of the longest substring without repeating 
characters.

"""


# PLAN
"""
Initial:
    - Go through the string building a substring
    - If there is a duplicate, the substring will remove everything before and
      including that duplicate letter
    - Then it will sort through the list of substrings to find the longest

Improved:
    - Make a window of two pointers
    - The right side progresses as it goes through the string
    - The left side progresses only if there's a duplicate letter
    - - The left side will then become the duplicate's index
    - While this is being done, the length of the window is compared and held
      for the longest value

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
    question_solution.initial_question(s="abcabcbb")
    question_solution.initial_question(s="bbbbb")
    question_solution.initial_question(s="pwwkew")

    # optimised QUESTION
    print("\n--- Optimised Answer ---")
    

def check_pipeline():                                                               # This is the pipeline that runs checks if required
    pass


# CLASSES 
class Solution:
    def initial_question(
            self, s: str
        ) -> int:
        # INITIATION
        substrings          = []

        current_substring   = ""
        longest_length      = 0

        # ITERATE THROUGH STRING
        for letter in s:
            # Guard Clauses
            if letter in current_substring:                                         #   # Found a repeating character
                
                substrings.append(current_substring)                                #   # Adds finished substrings to list

                last_letter_loc     = current_substring.rfind(letter)+1
                current_substring   = current_substring[last_letter_loc:]           #   # Make the new substring from the last repeat + 1
            
            # Append Letter
            current_substring += letter                                             #   # Add the letter to the current substring
        
        substrings.append(current_substring)

        # FIND LONGEST SUBSTRING
        for string in substrings:
            if len(string) > longest_length:                                        #   # Check and hold loop
                longest_length = len(string)

        return longest_length


    def optimised_question(
            self, s: str
        ) -> int:
        # INITIATION
        longest_length      = 0
        s_length_range      = range(len(s))                                         #   # Makes a list of index for s

        left_index          = 0

        char_dict           = {}

        # ITERATE THROUGH STRING
        for right_index in s_length_range:
            # Initialise
            letter = s[right_index]

            # Duplicate Letter
            if (letter in char_dict) and (char_dict[letter] > left_index):          #   # Checks if the letter has been used before if so, is newer
                left_index = char_dict[letter]                                      #   # Make the new index that letter
            
            # Answer Logic
            index_difference = right_index - left_index + 1
            
            if index_difference > longest_length:
                longest_length  = index_difference

            # Pointers Logic
            char_dict[letter]   = right_index + 1
        
        return longest_length




# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

