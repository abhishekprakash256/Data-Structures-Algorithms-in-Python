"""
The implementation of the modified binary search 
for the repetative element in the list
"""

from Binary_search import * 


class Modify_Sol(Solution):
    def return_val(self,lst,left,right):
        """
        The function to check for duplicate value and return val
        
        Args:
            lst (list): The list of the numbers 
            left: (int): The pointer index value
            right: (int): The pointer index value 
        
        Return:  
            index (int): The index value of the query  
        """

        while left <= right:

            mid = (left + right) // 2 

            if (lst[mid] == query and lst[mid - 1] != query) or (lst[mid] == query and lst[mid] == 0  ):
                return mid



    def modified_binary_search(self,lst,query)-> int:
        """
        The function to find the value in the list even repeated elements 
        Args:
            lst (list) : The sorted list of integers 
            query (int) : The query to find in the list 

        Returns:
            index (int) : The index value of the query 
        """

        left = 0 
        right = len(lst) - 1 

        while left <= right:

            mid = (left+right) // 2          

            if lst[mid] == query and mid !=0 and lst[mid-1] == query:
                self.return_val(lst,left,right)

            elif lst[mid] == query and lst[mid - 1] != query:
                return mid  
            
            elif lst[mid] < query:

                left = mid + 1

            else:
                right = mid - 1

        return -1

