n, t = input().split()
n = int(n)
t = int(t)

min = 100000000.0
max = 100100000.0
segments = []
i = 0
while i < n:
    d, s = input().split()
    d = int(d)
    s = int(s)
    if s < min:
        min = s
    segments.append((d, s))
    i += 1
min = -min

def function(c):
    ans = 0.0
    for segment in segments:
        d = segment[0]
        s = segment[1]
        ans += d/(s + c)

    return ans

ans = 0.0
while max-min > 0.000000001:
    c = (max + min)/2.0
    f = function(c)
    # if f == 10000:
    #     min += 1
    #     continue
    # fmin = function(min)
    # if fmin == 10000:
    #     min += 1
    #     continue
    # fmax = function(max)
    # if fmax == 10000:
    #     max -= 1
    #     continue
    # if fmin * fmax > 0:
    #     min += 1
    #     continue
    if f == t:
        # min = c
        break
    elif f > t:
        min = c
    else:
        max = c
    # c = (min + max)/2.0
    # print(c)
print("{0:.9}".format(c))