target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

acumulate=0
for number in range(2, target+1,2):
  if number%2==0:
    acumulate+=number

print(acumulate)