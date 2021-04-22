n = int(input())
dice = []
for i in range(n):
    dice.append(list(map(int, input().split())))
route = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
sumax = 0

for i in range(6):
    result = []
    tmp = [x for x in range(1, 7)]
    tmp.remove(dice[0][i])
    top = dice[0][route[i]]
    tmp.remove(top)
    result.append(max(tmp))
    for j in range(1, n):
        tmp = [x for x in range(1, 7)]
        tmp.remove(top)
        top = dice[j][route[dice[j].index(top)]]
        tmp.remove(top)
        result.append(max(tmp))
    result = sum(result)
    if sumax < result:
        sumax = result
print(sumax)

