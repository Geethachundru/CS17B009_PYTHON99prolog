my_list=[1,7,8,9,4,7,0,3,6,2,8,9,1,9]
list=[]
i=0
N=3
while i < len(my_list)-N:
    list.extend(my_list[i+N])
    i=i+1
list.extend(my_list[0:N])
print(list)
