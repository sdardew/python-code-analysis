def recursion(num):
    if num == 0:
        return 0
    return recursion(num - 1)

a = [1, 10, 5, 7, 6]
a.sort()
a.reverse()
a = sorted(a)

print(recursion(3))