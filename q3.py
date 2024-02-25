def Q3(a,b):
    if a<=0 or b<=0 or a>9 or b>9 or a>b:
        print("Please make sure the two arguments are between 1 and 9, and that the 2nd argument is greater than the 1st one.")
    elif a == 1:
        print(a, end=" ")
        c = b - a
        print(f"{c}"*c)
    else:
        print(f"{a}"*a, end=" ")
        c = b - a
        print(f"{c}"*c)
        return Q3(a-1,b)
