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

data = []
with open("data/day_2.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        row = np.array(list(map(int, row[0].split(" "))))
        data.append(row)

data = np.array(data, dtype=object)

MAX_DIFFERENCE = 3
MIN_DIFFERENCE = 1
safe = 0

def is_increasing(arr):
    return arr[0] < arr[-1]

def all_increase(arr):
    for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
    return True

def all_decrease(arr):
    for i in range(0, len(arr) - 1):
            if arr[i] < arr[i+1]:
                return False
    return True

def is_safe(arr):
    if is_increasing(arr):
        if all_increase(arr):
            for i in range(0, len(arr) - 1):
                first = arr[i]
                second = arr[i+1]
                difference = abs(second - first)
                if difference > MAX_DIFFERENCE:
                    return False
    elif not is_increasing(arr):
        if all_decrease(arr):
            for i in range(0, len(arr) - 1):
                first = arr[i]
                second = arr[i+1]
                difference = abs(second - first)
                if difference > MAX_DIFFERENCE:
                    return False
    return True


counter = 0
l = []
for d in data:
    if is_increasing(d) and all_increase(d):
        l.append(d)
    elif not is_increasing(d) and all_decrease(d):
        l.append(d)
print(len(l))

print(counter)


     
     
         
         
               
               
          




                    
                    
print(f"safe is: {safe}")





    

