def mult_down(n):
    if n == 0 :
        return 1
    return n * mult_down(n-1)
print(mult_down(4))
print(mult_down(7))