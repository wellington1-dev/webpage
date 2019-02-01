def greater_than(arr):

    mylist = []
    n = len(arr)
    for i in range(0,n):
        if(arr[i] > arr[1]):
            mylist.append(arr[i])
            print(len(mylist))

    return mylist


print(greater_than([6,8,9,10]))