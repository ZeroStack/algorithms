

    
if __name__ == "__main__":
    main()
    
def main():
    toSort = [6, 5, 3, 1, 8, 7, 2, 4]
    bubbleSort(toSort)
    
def bubbleSort(a):
    # number of numbers of times to iterate over main array
    n = len(a)
    
    # for every element in the array
    for i in range(n):
        # create a range n times with a diminishing n by i-1
        for j in range(n-i-1):
            # if the right element is larger than the left element
            if a[j] > a[j+1]:
                # display the array
                print("[",a[j],"]",">","[",a[j+1],"]")
                # swap the elements
                a[j], a[j+1] = a[j+1],a[j]
                # print array a at the end of swap
                print([i for i in a])
    
    # print array a at end
    print([i for i in a])
    




