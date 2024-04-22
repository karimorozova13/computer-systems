nums =  [1, 2, 3, 4, 5]
nums2 = [4, 5, 6,7,8]
sq_nums = list(map(lambda x: x**2, nums))

sum_arr = list(map(lambda x, y: x + y,nums, nums2 ))

print(sq_nums)
print(sum_arr)

#  list comprehensions
squared_nums = [x **2 for x in nums]
print(squared_nums)
