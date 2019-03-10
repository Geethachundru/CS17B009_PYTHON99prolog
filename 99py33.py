x=0
def gcd(a,b):
    if (a>b):
        r1=a
        r2=b
    else:
        r1=b
        r2=a   
    if(r1%r2==0):
        x=r2
    else:
        gcd(r2, r1%r2)
a= int(input("Enter a number"))
b= int(input("Enter a number"))
if x==1:
    print("they are coprimes")
else:
    print("they are not coprimes")
