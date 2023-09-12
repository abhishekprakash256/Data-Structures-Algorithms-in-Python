"""
The implementation of the modified binary search 
for the repetative element in the list
"""

from Binary_search import * 


class Modify_Sol(Solution):
    def modified_binary_search(self,lst,query)-> int:
        """
        The function to find the value in the list even repeated elements 
        Args:
            lst (list) : The sorted list of integers 
            query (int) : The query to find in the list 

        Returns:
            index (int) : The index value of the query 
        """

        