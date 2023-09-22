"""
To find the dupliacte number in the list 
using the fast and the slow pointer and without using the extra space 
"""

#test cases 


#test cases

test1 = {
	'input': [3,4,5,7,1,8,7],
	'output': 7
}

test2 = {
	'input': [0],
	'output': None
}

test3 = {
	'input': [1,2,3,4,4],
	'output': 4
}

test4 = {
	'input': [1,1,1,1,1,1],
	'output': 1
}


class Solution:
	def find_duplicate(self,dup_lst):
		"""
		The function to find the duolicate number in the list
		Args:
			duo_lst (list): The list of the numbers duolicate 
		Return:
			repeated_num (int) : the repeated number in the list
		"""

		if len(dup_lst) == 0 or len(dup_lst) == 0:
			return None

		slow = 0 
		fast = slow + 2
		count = 0
		length = len(duo_lst)

		while True:

			if duo_lst[slow] == duo_lst[fast]:

				count +=1
				slow = 0 

				if count == 2 :

					return fast

			slow +=1
			fast +=2

		return 

