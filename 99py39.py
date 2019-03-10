a=int(input("enter a number"))
b=int(input("enter a number"))
list=[]
if(a<b):
    r1=a
    r2=b
else:
    r1=b
    r2=a
j=r1
while (j<r2):
    i=1
    k=0
    while (i<=j):
        if((j%i)==0):
            k=k+1
            i=i+1
    if(k==2):
        list.append(j)
    j=j+1
print(list)
