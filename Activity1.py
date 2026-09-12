def sum_down(n):
    if n == 0:
        return 0
    return n + sum_down(n-1)
print("sum+down(3) = 3+2+1+0 = ", sum_down(3))
print("sum+down(7) = 7+6+5+4+3+2+1+0 = ", sum_down(7))
n = int(input("Enter a number : "))
print(sum_down(n)) 