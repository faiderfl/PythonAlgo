sorted_list = [1,3,4,5,7,8,12,16]

def binary_search(list_sort:list, index:int)->int:
    lower= 0
    higher= len(list_sort)-1
    while(lower<=higher):
        mid= int((lower + higher)/2)
        if(list_sort[mid]==index):
            return mid
        if(index<list_sort[mid]):
            higher=mid-1
        else:
            lower= mid+1
    else:
        return -1

      
    
    


print(binary_search(sorted_list, 5))