# Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the remaining elements have been shifted left to fill the emptied indices. Return the number of valid elements. Many languages have library functions for performing this operation-- you cannot use the functions.
# Hint - this is an O(n) time and O(1) space solution.

def delete_duplicates(A):
  i = 0
  while i<len(A)-2:
    if A[i] == A[i+1]:
      A.pop(i)
    else:
      i += 1

  return len(A)


print(delete_duplicates([1,1,3,2,2,2,5]))

####
def duplicates_5_6(arr):
  if not arr:
    return 0
  
  wi = 1
  for i in range(1, len(arr)):
    if arr[wi-1] != arr[i]:
      arr[wi] = arr[i]
      wi += 1

  return wi 

my_arr= [1,2,2,4]

my_carr= [1,1,1,1,5,3,2]
my_uber = [1,2,3,4,4,5,6,7,7,8,8,8,8,9]

a = duplicates_5_6(my_arr)
b = duplicates_5_6(my_carr)
c = duplicates_5_6(my_uber)
print(a, '\n', b, '\n', c)
