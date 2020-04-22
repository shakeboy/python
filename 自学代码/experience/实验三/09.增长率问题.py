r = 0.008
h = 13
i = 0
while 1:
    i += 1
    t = h
    h = t * (1 + r)
    if h > 26:
        break
print(i, "年后我国人口超过26亿")
