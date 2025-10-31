def func(n):
    if n == 1:
        return 1
    else:
        return func(n - 1) + func(n - 2)


for i in range(5):
    print(func(i), end=" ")
