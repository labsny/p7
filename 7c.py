l=[]
n=int(input("Enter number of values for num_list: "))
print("Enter the elements:")
for i in range(n):
    l.append(int(input()))
mean=sum(l)/len(l)
s=0
for i in l:
    s+=(i-mean)**2 
SD=(s/len(l))**0.5
print("Mean:",mean,"\nStandard Deviation:",SD)    
