# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height=0
number_heights=0
for height in student_heights:
  total_height+=height
  number_heights+=1
average_height=round(total_height/number_heights)

print(f"total height = {total_height}\nnumber of students = {number_heights}\naverage height = {average_height}")