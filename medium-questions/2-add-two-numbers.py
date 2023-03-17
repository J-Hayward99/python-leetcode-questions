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
from typing import Optional
from typing import ListNode

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
            self, l1: Optional[ListNode], l2: Optional[ListNode]
        ) -> Optional[ListNode]:
        
        def linked_list_to_number(list_node):                                       #   # DRY principle
            # INITIATION
            temp_string = ""
            
            # APPEND NODES TO LIST
            while True:
                # Character Append
                temp_string += str(list_node.val)                                   #   # Add value to string
                
                # Break Condition
                if list_node.next == None:                                          #   # If the list is finished, stop loop
                    break

                # Next Node
                list_node = list_node.next                                          #   # Next node

            # RETURN VALUE
            return int(temp_string[::-1])                                           #   # reverse string then cast string to an integer


        # INITIATION
        l1_number       = linked_list_to_number(l1)                                 #   # For first list
        l2_number       = linked_list_to_number(l2)                                 #   # For second list
        
        result_string   = str(l1_number + l2_number)                                #   # Add the numbers together then cast as a string
        result_string   = result_string[::-1]                                       #   # Reverse the string

        result_head     = ListNode()                                                #   # The dummy head used to start the list
        current_node    = result_head                                               #   # The instance used to make the list
        
        # STRING/NUMBER TO LINKED LIST
        for digit in result_string:                                                 #   # Iterate through the digits
            new_node            = ListNode(int(digit))                              #   # For the new node in the list, give it a value
            current_node.next   = new_node                                          #   # Make the new node the current node's next pointer
            current_node        = new_node                                          #   # Loop the system by making the new node the current one
    
    # ANSWER
        return result_head.next                                                     #   # Return the answer, using .next to avoid the head



    def optimised_question(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
        ) -> Optional[ListNode]:
        # INITIATION
        carried_number  = 0                                                         #   # Used for when a column digit is over 9

        result_head     = ListNode()                                                #   # The dummy head used to start the list
        current_node    = result_head                                               #   # The instance used to make the list

        # NODE ITERATION
        while (l1 or  l2 or  (carried_number != 0)):                                #   # If both nodes exist or the carry remains
            # Node Numbers
            l1_number       = l1.val if l1 else 0                                   #   # Use l1.val if l1 exists, if not, use 0
            l2_number       = l2.val if l2 else 0                                   #   # Use l2.val if l1 exists, if not, use 0

            # Acquired Column Sum
            column_sum      = l1_number + l2_number + carried_number                #   # For a given digit, calculate it's column sum

            # Acquire Carried Sum
            carried_number  = column_sum // 10                                      #   # Quotient of column sum divided by 10
            column_sum      = column_sum  % 10                                      #   # Remainder of column sum divided by 10

            # Next Result Node Footwork
            new_node            = ListNode(column_sum)                              #   # For the new node in the list, give it a value
            current_node.next   = new_node                                          #   # Make the new node the current node's next pointer
            current_node        = new_node                                          #   # Loop the system by making the new node the current one
            
            # Next Linked Lists Nodes Footwork
            l1 = l1.next if l1 else None                                            #   # Next node if it exists
            l2 = l2.next if l2 else None                                            #   # Next node if it exists

        # ANSWER
        return result_head.next                                                     #   # Return the answer, using .next to avoid the head




# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

