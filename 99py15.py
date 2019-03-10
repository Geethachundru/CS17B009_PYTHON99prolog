my_list=[1,6,8,8,0,2,5,7]
list=[]
for i in my_list:
    list.extend([i]*i)
print(list)
