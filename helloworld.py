#Script Begins

print("Sunny Rocks!")

a=4
print(a)
b=5
print(b)
print("b = a ? : ")
b=a 
print(a)

if b == a:
	print ("equal")
else:
	print("not equal")

# Function for checking the divisibility
# 

def checkDivisibility (a,b):
	if a%b == 0:
		print ("a is divible by b")
	else:
		print ("a is not divisible by b")


# Driver program to test the above func.

checkDivisibility(4,2)


#Script ends
