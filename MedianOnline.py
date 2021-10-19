from sys import stdin
def heapify(li, idx, n):
    # print('unsorted:', li)
    left = idx * 2 + 1
    right = idx * 2 + 2
    l_idx = idx
    if (left < n and li[left] > li[l_idx]):
        l_idx = left
    if (right < n and li[right] > li[l_idx]):
        l_idx = right
    if l_idx != idx:
        li[idx], li[l_idx] = li[l_idx], li[idx]
        return heapify(li, l_idx, n)

def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n//2 -1, -1, -1):
        heapify(unsorted, i, n)
    # print("after minheap", unsorted)
    for i in range(n-1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

cnt = int(stdin.readline())
for i in range(cnt):
    input_arr = list(map(int,stdin.readline().split()))
    arr_cnt = input_arr[0]
    arr_ele = input_arr[1:]

    min_heap = []
    max_heap = []
    sum = 0
    for j in range(arr_cnt):
        if len(min_heap) == 0 and len(max_heap) == 0:
            max_heap.append(arr_ele[j])
            print(min_heap, 'min')
            print(max_heap, 'max')
            print('=====')
            median = arr_ele[j]
        elif len(max_heap) != 0:
            if arr_ele[j] > max_heap[0]:
                min_heap.append(arr_ele[j])
                heap_sort(min_heap)
                print(min_heap, 'min')
                print(max_heap, 'max')
                print('=====')
            elif arr_ele[j] < max_heap[0]:
                max_heap.append(arr_ele[j])
                max_heap = heap_sort(max_heap)
                print(min_heap, 'min')
                print(max_heap, 'max')
                print('=====')

            if len(min_heap) == len(max_heap):
                median = (max_heap[0] + min_heap[0]) // 2
            elif len(min_heap)+1 == len(max_heap):
                median = max_heap[0]
            elif len(max_heap)+1 == len(min_heap):
                median = min_heap[0]

            elif len(min_heap) == len(max_heap)+2:
                max_heap.append(min_heap.pop(0))
                max_heap = heap_sort(max_heap)
                print(min_heap, 'min')
                print(max_heap, 'max')
                print('=====')
                median = (max_heap[0] + min_heap[0]) // 2
            elif len(max_heap) == len(min_heap)+2:
                min_heap.append(max_heap.pop(0))

                heap_sort(min_heap)
                print(min_heap, 'min')
                print(max_heap, 'max')
                print('=====')
                median = (max_heap[0] + min_heap[0]) / 2

        sum += int(median)
        print(int(median), 'med')
    print(str(sum)[-1])

    