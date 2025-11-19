def bubble_sort(list) -> list:
    unsorted_until_list = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_list):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                sorted = False
        unsorted_until_list -= 1
    return list

if __name__ == "__main__":
    print(bubble_sort([1,3,2,5,4]))