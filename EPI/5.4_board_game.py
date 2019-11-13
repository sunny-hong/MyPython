def board_game(A):
  res = False
  # check if the next destination is >0. If not, decrement one. 
  # -> current value, current index, next index, next value. 
  # next_index = current_index + current_value
  # next_value = A[next_index]
  # if next_value>0: okay 
  # example : A = [3,3,1,0,2,0,1]
  canyoujump = None     # index of value- where I check if we can jump to non-zero value or not.
  z_index = None        # zero index
  while 0 in A:
    print("while loop")
    z_index = A.index(0)
    canyoujump = z_index - 1
    A[canyoujump] -= 1
    del A[z_index]
    print(A)
    # reducing method. 
    # start from the end index to front
  
  return res

success1 = [3,3,1,0,2,0,1]
print(board_game(success1))

failure1 = [3,2,0,0,2,0,1]
print(board_game(failure1))

# still working on it.
