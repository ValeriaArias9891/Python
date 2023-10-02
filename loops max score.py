# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
score_max=0
for score in student_scores:
  if score_max<score:
    score_max=score
  else: 
    score_max= score_max
print(f"The highest score in the class is: {score_max}")