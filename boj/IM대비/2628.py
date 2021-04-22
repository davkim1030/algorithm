x0, x1, y0, y1 = 0, 1, 2, 3


# returns size of rectangle
def get_size(p):
    return (p[y1] - p[y0]) * (p[x1] - p[x0])


# input area
w, h = map(int, input().split())
cut_count = int(input())
cuts = []
for i in range(cut_count):
    cuts.append(list(map(int, input().split())))

# piece data [x0, x1, y0, y1]
pieces = [[0, w, 0, h]]
for c in cuts:
    tmp = pieces[:]
    for p in tmp:
        # case of parallel cut
        if c[0] == 0:
            if p[y0] < c[1] < p[y1]:    # if the cut is in y0 ~ y1 range
                pieces.append([p[x0], p[x1], p[y0], c[1]])
                pieces.append([p[x0], p[x1], c[1], p[y1]])
            else:
                pieces.append(pieces[0])
        # case of vertical cut
        else:
            if p[x0] < c[1] < p[x1]:    # if the cut is in x0 ~ x1 range
                pieces.append([p[x0], c[1], p[y0], p[y1]])
                pieces.append([c[1], p[x1], p[y0], p[y1]])
            else:
                pieces.append(pieces[0])
        pieces.pop(0)

# get biggest size
max_size = 0
for p in pieces:
    max_size = max(max_size, get_size(p))
print(max_size)

