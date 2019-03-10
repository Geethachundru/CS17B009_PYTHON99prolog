my_list=["bala",1,[9,[8]],7,["kittu","rishi"]]
output=[]
def removeNestings(my_list):
    for i in my_list: 
        if type(i) == list:
            removeNestings(i)
        else:
            output.append(i)

print('the original list: ',my_list)
removeNestings(my_list)
print('the list after removing nesting: ',output)
