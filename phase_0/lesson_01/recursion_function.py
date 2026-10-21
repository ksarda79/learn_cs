def mystery(n):
    if n == 0:
        return
    print("going down", n)
    mystery(n - 1)
    print("coming up", n)

mystery(3)
