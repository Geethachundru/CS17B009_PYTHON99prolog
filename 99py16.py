my_list=[1,3,7,8,9,0,4,9,3,6,0,2,1,0,2,5,0]
n=3
list=[]
i=0
while i < len(my_list):
    if (i+1)%3!=0:
        list.append(my_list[i])
        i=i+1
    else:
        i=i+1
print(list)
        
