lo, hi = 0, 1000
f = lambda x: x ** 2
target = 200

while lo < hi:
    mid = lo + hi >> 1
    if f(mid) < target:
        lo = mid + 1
    else:
        hi = mid

print(lo)


possible = lambda x: x < 100

while lo < hi:
    mid = lo + hi + 1 >> 1
    if possible(mid):
        lo = mid
    else:
        hi = mid - 1

print(lo)

