import datetime

(h, m, s) = list(map(int, input().split()))
s += 1
if s == 60:
    m += 1
    s = 0
if m == 60:
    h += 1
    m = 0
if h == 24:
    h = 0

print("%02d:%02d:%02d" % (h, m, s))

print((datetime.datetime(1000, 10, 1, h, m, s) + datetime.timedelta(seconds=1)).time())
