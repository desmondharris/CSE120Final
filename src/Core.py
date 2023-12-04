def is_basic_operand(operand):
    return operand in ["+", "-", "*", "/", "%", "^", "(", ")"]


def is_md(operand):
    return operand in ['/', '*']


def is_opening(operand):
    return operand in ["(", "[", "{"]


def is_closing(operand):
    return operand in [")", "]", "}"]


def n_th_root(n, x):
    return x ** (1/n)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def is_prime(n):
    for i in range(2, int(n)):
        if (n % i) == 0:
            return False
    return True


# function to convert to superscript taken from https://www.geeksforgeeks.org/python-convert-string-to-superscript/
# NOT written by students
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


def differentiate(polynomial, symbol):
    deriv = ""
    c3 = polynomial["c3"]*3
    deriv = deriv + f"{c3}{symbol}{get_super('2')}" if c3 != 0 else ""
    c2 = polynomial["c2"]*2
    deriv = deriv + f" + {c2}{symbol}" if polynomial["c2"] != 0 else deriv
    deriv = deriv + f" + {polynomial['c1']}" if polynomial["c1"] != 0 else deriv
    return deriv


def factor(n, num_factors=20):

    found = 0
    factors = []
    for i in range(1, int(n)):
        if n % i == 0:
            factors.append(i)
            found += 1
            if found == num_factors:
                return factors
    return factors







