def hanoi_tower(n, a, b, c, k, min_num, max_num):
    if n>0:
        if((max_num + min_num) % 2):
            mid = ((max_num + min_num) // 2) + 1
        else:
            mid = ((max_num + min_num) // 2) 

        if (min_num < k and k < mid) :
            hanoi_tower(n-1, a, c, b, k, min_num, mid)
        elif (k == mid):
            print(a, c)
        elif (mid < k and k <= max_num):
            hanoi_tower(n-1, b, a, c, k, mid, max_num)

num = int(input())
for i in range(num):
    inp = input()
    num_disks, k = (inp.split())
    num_disks = int(num_disks)
    k = int(k)
    max_num = 2 ** num_disks - 1
    hanoi_tower(num_disks, 1, 2, 3, k, 0, max_num)