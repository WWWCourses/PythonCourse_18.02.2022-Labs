

try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    if a > b and a > c:
        if c > b:
            b, c = c, b
    elif b >= c and b > a:
        a, b = b, a
        if c > b:
            b, c = c, b
    elif c > a and c > b:
        a, c = c, a
        if c > b:
            b, c = c, b
    print("a = {}, b = {}, c = {}".format(a, b, c))
except ValueError as err:
    print(err)
