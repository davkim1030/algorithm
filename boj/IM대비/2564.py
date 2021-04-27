NORTH, SOUTH, WEST, EAST = 1, 2, 3, 4

w, h = map(int, input().split())
n = int(input())
stores = []
for i in range(n):
    stores.append(list(map(int, input().split())))
user = list(map(int, input().split()))

result = 0
for s in stores:
    if s[0] == user[0]:
        result += abs(user[1] - s[1])
    elif s[0] == NORTH:
        if user[0] == SOUTH:
            left = user[1] + s[1]
            result += h + (left if left < 2 * w - left else 2 * w - left)
        elif user[0] == WEST:
            result += user[1] + s[1]
        elif user[0] == EAST:
            result += user[1] + w - s[1]
    elif s[0] == SOUTH:
        if user[0] == NORTH:
            left = user[1] + s[1]
            result += h + (left if left < 2 * w - left else 2 * w - left)
        elif user[0] == WEST:
            result += h - user[1] + s[1]
        elif user[0] == EAST:
            result += h - user[1] + s[1]
    elif s[0] == WEST:
        if user[0] == EAST:
            top = user[1] + s[1]
            result += w + (top if top < 2 * h - top else 2 * h - top)
        elif user[0] == NORTH:
            result += user[1] + s[1]
        elif user[0] == SOUTH:
            result += user[1] + h - s[1]
    elif s[0] == EAST:
        if user[0] == WEST:
            top = user[1] + s[1]
            result += w + (top if top < 2 * h - top else 2 * h - top)
        elif user[0] == NORTH:
            result += w - user[1] + s[1]
        elif user[0] == SOUTH:
            result += w - user[1] + h - s[1]

print(result)

