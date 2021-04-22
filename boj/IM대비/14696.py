star, circle, rect, tri = [x for x in range(4)]
n = int(input())

for i in range(n):
    tmp = list(map(int, input().split()))
    a = [0] * 4
    for j in tmp[1:]:
        a[4 - j] += 1
    tmp = list(map(int, input().split()))
    b = [0] * 4
    for j in tmp[1:]:
        b[4 - j] += 1
    result = str()
    if a[star] == b[star]:
        if a[circle] == b[circle]:
            if a[rect] == b[rect]:
                if a[tri] == b[tri]:
                    result = "D"
                else:
                    result = "A" if a[tri] > b[tri] else "B"
            else:
                result = "A" if a[rect] > b[rect] else "B"
        else:
            result = "A" if a[circle] > b[circle] else "B"
    else:
        result = "A" if a[star] > b[star] else "B"
    print(result)

