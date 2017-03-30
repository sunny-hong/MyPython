#Input s are the following:
#5 6 7
#3 6 10

import sys
a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]


#####
#a = [int(x) for x in raw_input().split()]
#b = [int(x) for x in raw_input().split()]

#print sum([1 for x in range(3) if a[x] > b[x]]), sum([1 for x in range(3) if a[x] < b[x]])
# #######
#A = list(map(int, raw_input().strip().split()))
#B = list(map(int, raw_input().strip().split()))
#Ascore = len([1 for a,b in zip(A,B) if a>b])
#Bscore = len([1 for a,b in zip(A,B) if b>a])
#print Ascore, Bscore
#####
#a0 = 5
#a1 = 6
#a2 = 7
#b0 = 3
#b1 = 6
#b2 = 10

A = [a0, a1, a2]
B = [b0, b1, b2]
Alice = 0
Bob =0

for count in range(0, 3):
    if A[count]> B[count]:
        Alice =Alice+1
    elif A[count] < B[count]:
        Bob = Bob+1
    
print (Alice, Bob)
