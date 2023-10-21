# a = 10
# b = 5
# c = a + b
# print("result=", c)
# c1 = a + b
# c2 = a - b
# c3 = a * b
# c4 = a/b
# c5 = a ** b
# c6 = a % b
# print("Result=", c1)
# print("Result=", c2)
# print("Result=", c3)
# print("Result=", c4)
# print("Result=",c5)
# print ("Result=", c6 )

a1 = 10
a2 = 5
a3 = 15
a4 = 50
result = a1 > a2
print("Result=", result)
# and or not
result2 = a1 > a2 and a1 < a3
r1 = a1 > a2
r2 = a1 < a3
print("R1 a1 > a2", r2)
print("R2 a1 < a2", r2)
print("R=", r1,r2)

print("and, or,-->result", result2)
print()
if(r1):
    print("TRue item1")
else:
    print("False item2")

if a1 >= 10:
    print('True item 1')
elif a1 < a2:
    print ('True item 3')
else:
    print ('False item 2')


