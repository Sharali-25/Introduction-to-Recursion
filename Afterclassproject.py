# part 1 summing up the numbers using recursion
def sum_down(o):
    if o == 0:
        return 0
    return o + sum_down(o-1)
print("sum+down(3) = 3+2+1+0 = ", sum_down(3))
print("sum+down(7) = 7+6+5+4+3+2+1+0 = ", sum_down(7))
s = int(input("Enter a number : "))
print(sum_down(s)) 
# part 2 
def mult_down(m):
    if m == 0 :
        return 1
    return m * mult_down(m-1)
print(mult_down(6))
print(mult_down(2))
o = int(input("Enter a number : "))
print(mult_down(o))
# part 3
def sum_down(p):
    if p == 0:
        return 0
    return p + sum_down(p-1)
print("", sum_down(3),"This uses 3 frames")
print("", sum_down(7),"his uses 7 frames")
j = int(input("Enter a number : "))
print(sum_down(j)) 