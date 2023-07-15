# DESCRIPTION
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

"""


# PLAN
"""
Initial:
    - Make hashmaps of all rLetters and rPairs.
    - Iterate through string.
    - If its a pair, add it and skip next iteration.
    - If its a char, add it.

Optimised:
    - Roman numbers work such that each "digit" is it's own letter.
    - Hence if a smaller number is smaller than a bigger number, it's inherently
      a pair.
    - And the pair is "bigger number - smaller number" so one can just subtract
      the smaller after adding the bigger.
    - Because the way the code is, the number isn't checked for being the 
      smaller of a pair, only if it's the bigger, so you have to subtract the
      smaller number twice.

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
        ) -> int:
        # INTITATION
        # Dictionaries
        number_hashmap = {
            "I"  : 1,
            "V"  : 5,
            "X"  : 10,
            "L"  : 50,
            "C"  : 100,
            "D"  : 500,
            "M"  : 1000
        }
        special_pairs = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }

        # Variables
        cummulative = 0
        special     = special_pairs.keys()
        length_s    = len(s)
        bool_skip   = False
        
        # ITERATE
        for index, char in enumerate(s):
            # Last Character Check
            if index == length_s and not bool_skip:
                cummulative += number_hashmap[char]
                break
            
            # Skip Check
            if bool_skip:
                bool_skip = False
                continue

            # Pair Check
            pair = s[index:index + 2]
            
            if pair in special:
                cummulative += special_pairs[pair]
                bool_skip = True
            else:
                cummulative += number_hashmap[char]
        
        return cummulative



    def optimised_question(
            self, s:str
        ) -> int:
        number = {
            "I"  : 1,
            "V"  : 5,
            "X"  : 10,
            "L"  : 50,
            "C"  : 100,
            "D"  : 500,
            "M"  : 1000
        }
        
        range_s     = range(1, len(s))                                              #   # Skips first element since can assign it to cummulative
        cummulative = number[s[0]]
        
        # Iterate
        for index in range_s:
            char            = s[index]
            previous_char   = s[index - 1]
            cummulative     += number[char]

            # Pair Check
            if (number[previous_char] < number[char]):
                cummulative -= 2*number[previous_char]
        
        return cummulative




# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

