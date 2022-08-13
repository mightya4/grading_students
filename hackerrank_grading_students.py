#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    len_of_grades = len(grades)
    array_of_grades = []
    for i in range(0, len_of_grades):
        current_grade = grades[i]
        tmp_val = 0
        if grades[i] > 37:
            if grades[i] % 10 > 5 and abs(grades[i] % 10 - 10) < 3:
                tmp_val = current_grade + abs(grades[i] % 10 - 10)
            elif grades[i] % 10 < 5 and abs(grades[i] % 10 - 5) < 3:
                tmp_val = current_grade + abs(grades[i] % 10 - 5)
            else:
                tmp_val = grades[i]
        else: tmp_val = grades[i]

        array_of_grades.append(tmp_val)
    return array_of_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
