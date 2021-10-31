#Linear and Binary Search Algorithm

#Linear Search Algorithm
def linear_search(number_list, number_to_find):
    #code
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return "Not Found"

#Binary Search Algorithm
def binary_search(number_list, number_to_find):
    #code
    left_index = 0
    right_index = len(number_list) -1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        elif mid_number < number_to_find:
            left_index = mid_index + 1
            
        else:
            right_index = mid_index - 1

    return "Not Found"


if __name__ == '__main__':
    number_list = [12,15,17,19,21,24,45,67]
    number_to_find = int(input("Number to Find"))

    #index = linear_search(number_list, number_to_find)
    index = binary_search(number_list, number_to_find)
    
    #print(f"Number found at {index} using Linear Search")
    print(f"Number found at {index} using Binary Search")
