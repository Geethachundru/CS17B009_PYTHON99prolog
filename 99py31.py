n=34
i=1
count=0
while i < n:
    if n%i==0:
        count=count+1
        i=i+1
    else:
        i=i+1
if count>2:
    print("it is not a prime")
else:
    print("it is a prime")
    
    
