my_list=[1,1,2,4,6,6,7,9,4,6,6,0]
def pack(my_list):
    list1=[]
    for i in my_list:
        if my_list[i]=my_list[i+1]:
            count=count+1
            del my_list[i+1]

