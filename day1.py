import numpy as np

import csv

#------------------------------ Day 1 ---------------------------------#
first_array = np.array([])
second_array = np.array([])
with open("data/input.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        l = row[0]
        numbers = l.split()
        n1, n2 = numbers[0], numbers[1]
        first_array = np.append(first_array, int(n1))
        second_array = np.append(second_array, int(n2))

first_array.sort()
second_array.sort()

def computes_distance_lists(l1, l2):
    return int(sum(np.abs(l2 - l1)))

total_distance = computes_distance_lists(first_array, second_array)
print(total_distance)

def computes_similarity_score(l1, l2):
    similarity_score = 0
    for l in l1:
        similarity_score += (l * sum(l2 == l))
    print(similarity_score)
    return similarity_score
computes_similarity_score(first_array, second_array)

#------------------------------ Day 2 ---------------------------------#

data = np.array([])
with open("data/day_2.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        data = np.append(data, row[0])
        data = data.reshape(len(data), 1)

MAX_DIFFERENCE = 3
safe = 0
print("safe is", safe)
for i, nums in enumerate(data):
    nums = np.array(nums[0].split())
    nums = nums.astype(int)
    nums_ascending = np.sort(nums)
    nums_descending = np.sort(nums)[::-1]
    if np.array_equal(nums, nums_ascending) or np.array_equal(nums, nums_descending):
        for i, n in enumerate(nums):
            if i < (len(nums) - 1):
                dif = abs(n - nums[i + 1])
                if dif > MAX_DIFFERENCE:
                    safe += 1
                    break
                    
                    
print(f"safe is: {safe}")





    

