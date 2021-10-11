def calculate(a, b):
    if b > 0:
        i = a % b
        j = b
        return calculate(j, i)
    elif b == 0:
        return a

cnt = int(input())
for i in range(cnt):
    inp = input()
    n, m = inp.split()
    n = int(n)
    m = int(m)
    if n > m :
        larger = n
        smaller = m
    else :
        larger = m
        smaller = n

    answer = calculate(larger, smaller)
    print(answer)