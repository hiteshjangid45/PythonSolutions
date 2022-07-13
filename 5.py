#    5

def remove_nulls(list1):
    for i in list1:
        if i=='null' or i=='nill':
            continue
        elif isinstance(i,list):
            remove_nulls(i)  # using recursion method 
        else:
            newlist.append(i)
    
list1=[1,[2,3,'null',4],['null'],5]
print("Original List : ",list1)
newlist=[]
remove_nulls(list1)
print("List without null/nill is : ",newlist)
