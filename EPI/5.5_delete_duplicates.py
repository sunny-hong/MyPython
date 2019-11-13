def delete_duplicates(A):
  i = 0
  while i<len(A)-2:
    if A[i] == A[i+1]:
      A.pop(i)
    else:
      i += 1

  return A


print(delete_duplicates([1,1,3,2,2,2,5]))
