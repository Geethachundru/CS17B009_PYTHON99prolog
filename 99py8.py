my_list=[1,7,8,8,9,9,3,5,7,7,9,4,2,0]
i=0
while i < len(my_list)-1:
    if my_list[i] == my_list[i+1]:
        del my_list[i]
    else:
        i = i+1
print(my_list)
