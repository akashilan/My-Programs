def insertElement(list1, pos, ele):
    """This function inserts an element(ele) in a list(list1) at the given position(pos) without using inbuilt methods."""
  
    list1.append(list1[-1])
    for i in range(len(list1)-2, pos-1, -1):
        list1[i+1] = list1[i]
        
    list1[pos] = ele
