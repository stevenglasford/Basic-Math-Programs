import math

print ("Please enter your variables")
print ("What is your 'a' value?")
a = input()
print("What is your 'b' value?")
b = input()

print("What is your 'c' value?")
c = input()

print("Discrinimate")
d = (b*b-4*a*c)

print(d)

if d < 0:
	print("There are no real ansers")

if d == 0:
	print("There is but a single answer")
	x = ((-b)/(2*a))
	print(x)

if d > 0:
	print("There are 2 real answers")
	m = ((-b+math.sqrt(d))/(2*a))
	n = ((-b-math.sqrt(d))/(2*a))
	print(m)
	print(n)
