N1 = 39
N2 = -34
operator = "*"

if operator == "+":
    result = N1 + N2
    even_odd =  "even" if result % 2 == 0 else "odd"
    print("{} {} {} = {} - {}".format(N1, operator, N2, result, even_odd))
elif operator == "-":
    result = N1 - N2
    even_odd = "even" if result % 2 == 0 else "odd"
    print("{} {} {} = {} - {}".format(N1, operator, N2, result, even_odd))
elif operator == "*":
    result = N1 * N2
    even_odd =  "even" if result % 2 == 0 else "odd"
    print("{} {} {} = {} - {}".format(N1, operator, N2, result, even_odd))
elif operator == "/":
    result = N1 / N2
    print("{} / {} = {}".format(N1, N2, result))
elif operator == "%":
    result = N1 % N2
    print("{} % {} = {}".format(N1, N2, result))
