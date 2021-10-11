import sys
sys.setrecursionlimit(10 ** 6)
num = int(input())
for i in range(num):
    inp = input()
    arr_H = list(map(int, inp.split()))[1:]
    arr_L = list(map(int, inp.split()))[1:]
    comparison_H = 0
    swap_H = 0
    comparison_L = 0
    swap_L = 0


    def quicksort_H(A, low, high) :
        if low >= high:
            return
        p = partition_Hoare(A, low, high)
        quicksort_H(A, low, p)
        quicksort_H(A, p+1, high)

    def quicksort_L(A, low, high) :
        if low >= high:
            return
        p = partition_Lumuto(A, low, high)
        quicksort_L(A, low, p-1)
        quicksort_L(A, p+1, high)

    def partition_Hoare(A, low, high) :
        global comparison_H, swap_H
        pivot = A[low]
        i = low - 1
        j = high + 1
        while True :
            while True:
                i += 1
                comparison_H += 1
                if (A[i] < pivot):
                    continue
                break
            while True:
                j -= 1
                comparison_H += 1
                if (A[j] > pivot):
                    continue
                break
            if i < j:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                swap_H += 1
            else : 
                return j

    def partition_Lumuto(A, low, high) :
        global comparison_L, swap_L
        pivot = A[low]
        j = low
        for i in range(low+1, high+1):
            comparison_L += 1
            if A[i] < pivot:
                j = j+1
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                swap_L += 1

        pivot_pos = j
        temp = A[low]
        A[low] = A[pivot_pos]
        A[pivot_pos] = temp
        swap_L += 1
        return pivot_pos

    quicksort_H(arr_H, 0, len(arr_H) - 1)
    quicksort_L(arr_L, 0, len(arr_L) - 1)
    print(swap_H, swap_L, comparison_H, comparison_L)