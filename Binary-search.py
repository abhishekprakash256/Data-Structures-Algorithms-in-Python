"""
implemement the binary search on the for the card problem 
"""

"""
make the search for the element in the stack and retuirn the position on the value

brute force appraoch 

do a linear scan and spit out the reslut for the position 

"""


#test cases 

test1 = {
	'input': {
	'cards': [13,11,10,9,8,7,5,2],
	'query':7
	},

	'output': 5
}



test2 = {
	'input': {
	'cards': [15,12,10,9,8,6,5],
	'query':12
	},

	'output':1
}


#repeated characters 
test3 = {
	'input': {
	'cards': [13,11,10,10,10,10,10],
	'query':10
	},

	'output': 2 
}


#no elemnt in the list
test4 = {
	'input': {
	'cards': [13,11,10,9,7,8],
	'query':24
	},

	'output': -1
}




class Solution:

	def find_element_brute_force(self,lst,query)-> int:
		"""
		The function to find the elemnt with brute force searching 
		Args:
			lst (list) : list of the elements
			query (int) : The element to search for 
		Return: 
			pos (int) : The index value of the element 
		"""

		indx = 0 

		while indx <= len(lst) - 1 :

			if lst[indx] == query:

				return indx

			indx +=1

		return -1









if __name__ == "__main__":
	sol = Solution()

	res = sol.find_element_brute_force(test1['input']['cards'], test1['input']['query'])
	res2 = sol.find_element_brute_force(test2['input']['cards'], test2['input']['query'])
	res3 = sol.find_element_brute_force(test3['input']['cards'], test3['input']['query'])
	res4 = sol.find_element_brute_force(test4['input']['cards'], test4['input']['query'])

	print(res == test1['output'])
	print(res2 == test2['output'])
	print(res3 == test3['output'])
	print(res4 == test4['output'])