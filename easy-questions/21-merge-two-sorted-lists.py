# DESCRIPTION
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

"""


# PLAN
"""
Initial:
    - Make head.
    - While-loop through both lists until all are complete.
    - As this happens, find the smallest current node of each list then add to 
      output one.
    - Return list.

Optimised:
    - If one list is empty, it's inherently the other list
    - The new node creation can be streamlined

"""


# IMPORTS
from typing import ListNode, Optional

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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def initial_question(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Start Node
        current_node    = ListNode()
        head_node       = current_node

        # Empty Lists Check
        if not (list1 or list2):
            return None
        
        while list1 or list2:
            # If list1 is Complete
            if not list1:
                node_val    = list2.val
                list2       = list2.next
            
            # If list2 is Complete
            elif not list2:
                node_val    = list1.val
                list1       = list1.next          

            else:
                # Find Smallest Variable
                if list1.val <= list2.val:
                    node_val    = list1.val
                    list1       = list1.next
                
                else:
                    node_val    = list2.val
                    list2       = list2.next

            # Make node
            current_node.val    = node_val
            new_node            = ListNode()
            
            # Stops Appending Tail Node if Complete
            if (list1 or list2):
                current_node.next   = new_node
                current_node        = new_node        
 
        return head_node



    def optimised_question(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_list    = ListNode()
        head_node       = current_list

        # No Lists
        if not (list1 or list2):
            return None

        # Only One List
        if not list1:
            return list2
        if not list2:
            return list1
        
        while list1 or list2:
            # If list1 is Complete
            if not list1:
                current_list.next   = list2
                break
            
            # If list2 is Complete
            elif not list2:
                current_list.next   = list1
                break          

            else:
                # Find Smallest Variable
                if list1.val <= list2.val:
                    current_list.next   = ListNode(list1.val, current_list)
                    current_list        = current_list.next 
                    list1               = list1.next
                
                else:
                    current_list.next   = ListNode(list2.val, current_list)
                    current_list        = current_list.next 
                    list2               = list2.next

        return head_node.next




# FUNCTIONS



# MAIN
main_pipeline()                                                                     # Runs the main pipeline

