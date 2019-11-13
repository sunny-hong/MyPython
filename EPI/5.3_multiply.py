# Write a program that takes two arrays representing integers, and returns an integer representing their product. For example, since 193707721 * -761838257287 = -147573952589676412927 if the inputs are [1,9,3,7,0,7,7,2,1], your function should return the following array: [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7]. Hint - use arrays to simulate the grade-school multiplication algorithm.   

# Same as the book answer 

def multiply(num1, num2):
  sign = None
  if (num1[0]<0) ^ (num2[0]<0):
    sign = -1
  else:
      sign = 1
  num1[0] = abs(num1[0])
  num2[0] = abs(num2[0])
  res = [0] * (len(num1)+len(num2))

  for i in reversed(range(len(num1))):
    for j in reversed(range(len(num2))):
      res[i+j+1] += num1[i]*num2[j]
      res[i+j] += res[i+j+1] // 10
      res[i+j+1] %= 10
  res = res[next((i for i, x in enumerate(res) if x!= 0), len(res)):] or [0]
  
  return[ res[0]*sign] + res[1:]


a = [-5,3,1]
b = [2,3,4]
print(multiply(a,b), -531*234)
a = [1,4,3,2,1,4,3,5,2,3,4,1,8,6,4,4]
b = [7,5,3,5,2,3,7,2,1,6,9,0]
print(multiply(a,b), 1432143523418644*753523721690)
a = [-9,9,1,3,6,7,5,3]
b = [-7,5,3]
print(multiply(a,b), -99136753*-753)
a = [7,5,0]
b = [6,0]
print(multiply(a,b), 750*60)
a = [2,4,7,1,9]
b = [-5,1,2,3]
print(multiply(a,b), 24719*-5123)

