# DESCRIPTION # FIXME currently doing
"""
Given a string s, find the length of the longest substring without repeating 
characters.

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
    - Get the first repeating letter's locations

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
    # question_solution.initial_question(s="bbbbb")
    # question_solution.initial_question(s="pwwkew")

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
        rep_letters_loc     = [0]   #   # Finds repeated character, zero to help get strings
        raw_substrings      = []    #   # Substrings between repeated character


        # GET REPEATING LETTERS
        for character in range(len(s)-1):         #   # Index of characters excluding first and last one
            print(s[character])
            if s[character] == s[character+1]:      #   # If current character is equal to the next one
                rep_letters_loc.append(character+1)


        # GET SUBSTRINGS
        for cur_index in rep_letters_loc:
            # Make Substring            
            if cur_index == rep_letters_loc[-1]:
                substring = (
                    s[cur_index:]
            )
            else:
                substring = (
                    s[cur_index:cur_index+1]
            )
            # Conditions             
            if substring == "":                 #   # Empty cases
                continue

            if substring in raw_substrings:     #   # Repeated cases
                continue
            
            # Append
            raw_substrings.append(substring)
        


        print(raw_substrings)
        print(len(max(raw_substrings)))


    def optimised_question(
            self, 
        ):
        pass




# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

