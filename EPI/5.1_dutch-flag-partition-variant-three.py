def array_three(A):
  if len(A)<1:
    return A
  store, store2, i = [A[0]], [], 0
  A = A[1:]
  while i<len(A):
    if A[i] in store:
      store.append(A.pop(i))
    else:
      if store2 == []:
        store2 = [A.pop(i)]
      elif A[i] in store2:
        store2.append(A.pop(i))
      else:
        i += 1
  return A+store+store2


my_arr = [1,5,4,5,1,4,4]
print(array_three(my_arr))
my_arr2 = [3,2,1,3,2,2,1,2,3,3,2,1,3,3,3,2,2,2,3,3,2,3,1,2,3,2,1,3,2,1,1,2,3,2,3,2,1,2,3,2,1,2,3,2,2,2,2,2,3,3,3,1,2,2,1,1,2,3]
print(array_three(my_arr2))
my_arr3 = [1]
print(array_three(my_arr3))
my_arr4 = []
print(array_three(my_arr4))
