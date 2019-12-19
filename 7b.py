l=[]
n=int(input("Enter number of values for l: "))
print("Enter the elements:")
for i in range(n):
    l.append(int(input()))
mode={}
for i in l:
    mode.setdefault(i,0)
    mode[i]+=1
k=list(mode.keys())
v=list(mode.values())
m=0
for i in mode:
    if m <= mode[i]:
    	m = mode[i]
md=k[v.index(m)]
print("mode =",md)
