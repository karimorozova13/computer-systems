from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  

words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence) 

numbers = [10, 4, 25, 7, 31]
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num) 
