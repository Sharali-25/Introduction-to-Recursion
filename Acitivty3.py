def sum_down(n):
    if n == 0:
        return 0
    return n + sum_down(n-1)
print("", sum_down(3),"This uses 3 frames")
print("", sum_down(7),"his uses 7 frames")
n = int(input("Enter a number : "))
print(sum_down(n)) 