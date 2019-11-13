# 5.2 INCREMENT AN ARBITRARY-PRECISION INTEGER
# Write a program which takes an input as array of digits encoding a nonnegative decimal integer D and updates the array to represent the inter D+1. For example, if the input is [1,2,9] then you should update the array to [1,3,0]

def plus_one(num_array):
  # 1. loop through array A... from end to front
  # 2. Variables: have "carry" and if adding 1 gives 10 or above, carry becomes from 0 to 1! 
  # have "ultimate_carry" as True
  # 3. if carry is present, add one to the higher decimal, and then carry equals false. if the added num is 10 or above, carry equals true.
  # 4. continue 3.
  # 5. if carry is True, but you're at the end of the array, outside of the loop, check if carry && ultimate_carry is True. If so, add an extra value 1 at the front of the array and return.

  carry, ultimate_carry = False, True
  my_len = len(num_array)
  if my_len<1:
    return num_array 
  num_array[my_len-1] += 1
  for i in reversed(range(my_len)): 
    # reversed() => if len(A) is 3, then it will loop 2,1,0
    if num_array[i]>=10:
      carry = True
      num_array[i] -= 10
      if (i-1 > 0) and (carry == True):
        num_array[i-1] += 1
        carry = False
    else:
      break
# check if there is a carry_out and another digit has to be added
  if (ultimate_carry & carry) == True:
    num_array = [1]+[0] + num_array[1:]
  

  return num_array

# print(plus_one([3,4,5,6]))
# print(plus_one([1,3,9]))
# print(plus_one([0]))
# print(plus_one([]))
# print(plus_one([9,9,9,9,9]))



def plus_one_ver2(num_array):
  # book's solution. 
  num_array[-1] += 1
  for i in reversed(range(1, len(num_array))):
    if num_array[i] == 10:
      num_array[i]=0
      num_array[i-1] += 1
    else:
      break
  if num_array[0] == 10:
    num_array[0]=0
    num_array = [1]+num_array

  return num_array


print(plus_one_ver2([3,4,5]))
print(plus_one_ver2([9,9,9]))

# Variant: 
# Write a program which takes as input two strings 's' and 't' of bits encoding binary numbers B_s, B_t, respectively, and returns a new string of bits representing number B_s + B_t.

def plus_one_variance(string_s, string_t):
  # convert string to array of integers
  # In a loop from back to front, add number of each index. if there is carry, add carry to the next forward index ()
  # At the end of the loop if there is still carry left, create a new digit/s and combine new digit array and original num_array
  len_s = len(string_s)
  len_t = len(string_t)
  if len_s<1:
    return string_t
  elif len_t<1:
    return string_s

  # separates string characters into an array. still string.
  s = list(string_s)
  t = list(string_t)

  # matches the length of variables, s and t. 
  temp = [0]
  if len_s > len_t :
    temp = temp * (len_s - len_t)
    t = temp + t
  elif len_t > len_s:
    temp = temp * (len_t - len_s)
    s = temp + s
  
  carry = 0
  res = []
  for i in reversed(range(1,len(s))):
    temp = int(s[i]) + int(t[i]) + carry 
    carry = 0
    if temp > 1:
      carry = int(temp/2)
      temp = temp%2
      res = [temp]+res
    else:
      res = [temp]+res

  temp = int(s[0])+ int(t[0]) + carry
  if temp>1:
      temp = temp%2
      res = [1]+[temp]+res
  else:
    res = [temp]+res
  
  temp = ""
  for i in res:
    temp+= str(i)

  return temp

a = "111"
b = "111"
print(plus_one_variance(a,b))
print(plus_one_variance("111011","101"))
print(plus_one_variance("11111111",""))
print(plus_one_variance("11111111","10"))
