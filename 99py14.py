my_list=[1,4,5,6,7,7,9,0,3]
list=[]
for i in my_list:
    list.extend([i,i])
print(list)
