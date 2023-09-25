"""
Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

print(lst1.pop(0))

"""

#-----------------problem in poppin the elements of the stack 

#for this question we need to make a deccreasing monotonic queue 


#test cases

lst1 = [4,5,2,4,4,6,1,7,8,0]


lst2 = [8,6,4,7,0,1,4,3,6,4]



class Solution:
	def decrease_queue(self,lst):
		"""
		The function to make the decreasing queue


		"""
		lst_queue = []

		#append the first value 
		lst_queue.append(lst[0])

		#start the comparision and popping 

		for i in range(1,len(lst)-1):

			while True:

				print(lst_queue)

				if lst_queue[len(lst_queue)-1] > i:

					lst_queue.append(i)

				else:
					lst_queue.pop(0)

		return lst_queue 


if __name__ == "__main__":
	sol = Solution()
	res = sol.decrease_queue(lst2)

	print(res)