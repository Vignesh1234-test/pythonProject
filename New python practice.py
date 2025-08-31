'''salary=int(input("Enter the Salary:"))
age=int(input("Enter the age:"))
if(salary>=20000 or age<=25):
    print("You are eligible for loan")
    loan=int(input("Enter the loan amt"))
    if(loan>50000):
        print("You cross the limt")
    else:
        print("You are eligibl for loan")
else:
    print("You are not eligible")'''

#List:

'''a=[1,2,3,3,3]
b=[2.34,3]
a.extend(b)
print(a)'''

#Tuple>>   it will not modify edit or delete
c=(1,2,2,3,4)
d=list(c) #cascading converting yuple into list
d[0]=22 #Modifying the values
print(d)
#Set >> it will not allow to modify but  able to add or delete
l={1,4,6,9}
#l.add(5)
#l.remove(6)
l.pop()
print(l)

#l[0]=34 #it will not allow to modify
print(l)