#
# #Funnction
#
# ll = [11,22,33,44,55,66]
# def f1():
#     print('F1 Hello')
#
# f1()
# f1()
# f1()
#
# for i in ll:
#      print ('i = ',i)

def f2(age,salary):

    long_salary = age * salary

    return long_salary
f2(2,500)
long_s1 = f2(2,500)
long_s2 = f2(3,500)
long_s3 = f2(4,500)
long_s4 = f2(5,500)
sal_s = [long_s1,long_s2,long_s3,long_s4]

print('long_s =',sal_s)

