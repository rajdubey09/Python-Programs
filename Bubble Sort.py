#Bubble Sort

def bubble_sort(number_list):
    size = len(number_list)
    
    for i in range(size-1):
        #swapped = False
        for j in range(size-1-i):
            if number_list[j] > number_list[j+1]:
                tmp = number_list[j]
                number_list[j] = number_list[j+1]
                number_list[j+1] = tmp
                #swapped = True

         #if not swapped:
             #break
            
    return number_list            

if __name__ == '__main__':

    number_list = [5,9,2,1,67,34,88,34,8,7,9]
    #number_list = [1,2,7,8,9]
    res = bubble_sort(number_list)
    print("Sorted List",res)
