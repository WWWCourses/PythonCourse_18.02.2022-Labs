import math

try:
    input_vars = input("Enter three vars for a, b and c in this format: a, b, c ") # a,b,c
    replaced_empty_spaces = input_vars.replace(" ", "") # a,b,c
    splitted_vars = replaced_empty_spaces.split(",")
    a, b, c = int(splitted_vars[0]), int(splitted_vars[1]), int(splitted_vars[2])

    print("a = {}".format(a))
    print("b = {}".format(b))
    print("c = {}".format(c))
    d = b * b - 4 * a * c
    if d < 0:
        print("\nD={0}\nThere are no real roots.".format(d))
    elif d == 0:
        x1 = -b / 2 * a
        print("\nX={0}".format(x1))
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("\nX1={0}\nX2={1}", x1, x2)
except ValueError as err:
    print(err)

