classnumber=int(input("enter the number of students: "))
TAB=[]
s=0
for i in range(classnumber):
    marks=int(input(f"enter the marks of student number {i+1} : "))
    TAB.append(marks)
    s=s+marks

m=s/len(TAB)
M= int(m)

print(f"the avreage is {M}")
for i in range(classnumber):
    if TAB[i]>=M:
        print(f"student {i+1} passed")
    else:
        print(f"student {i+1}failed")