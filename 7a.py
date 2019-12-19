a={}
n=eval(input("Enter the number of inputs: "))
no,p,c,m,b=[],[],[],[],[]
for i in range(n):
    no.append(int(input("Enter the serial number: ")))
    p.append(float(input("Enter physics marks: ")))
    c.append(float(input("Enter chemistry marks: ")))
    m.append(float(input("Enter math marks: ")))
    b.append(float(input("Enter bio marks: ")))
for i in range(n):
    a[no[i]]=[p[i],c[i],m[i],b[i]]
for i in a:
    print(i,"==>",end=" ")
    for j in a[i]:
        print(j,end=" ")
    print()
print()

tot={}
for i in a:
    tot[i]=sum(a[i])
for i,j in sorted(tot.items(),key=lambda a:a[1]):
    print(i,"==>",j)

details={}
for i in m:
    details[i]=[]
    for j in a:
        if(i==a[j][2]):
            details[i].append(j)
print(details)

