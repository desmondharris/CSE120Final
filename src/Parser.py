from Core import *
import logging


def lex(expression: str):
    '''
    Converts a string expression into a list of tokens
    :param expression: string fetched from Calculator
    :return: list of all legal tokens in expression
    '''

    temp = ""
    tokens = []
    decimal = False

    for i in range(len(expression)-1):

        l = expression[i]

        if l.isdigit():
            # Check if the first number is multi-digit or a decimal
            if expression[i+1].isdigit() or temp or expression[i+1] == '.':
                temp += l
                continue
            tokens.append(float(l))

        elif is_basic_operand(l):
            if temp:
                temp = float(temp)
                tokens.append(temp)
                temp = ""
                # We know any decimal is finished
                decimal = False
            tokens.append(l)
        elif l == '.':
            if decimal:
                logging.warning("Multiple decimal points in one number")
            else:
                decimal = True
                temp += l
        else:
            logging.warning(f"Unknown character '{l}'")


    if expression[-1].isdigit():
        # Check if the last two characters are a two-digit number
        if expression[-2].isdigit() or expression[-2] == '.':
            # If it's a decimal, we've already started building temp
            if decimal:
                tokens.append(float(temp + expression[-1]))
            # If not, we can ignore temp
            else:
                tokens.append(float(expression[-2:]))
        else:
            tokens.append(float(expression[-1]))

    elif is_basic_operand(expression[-1:]):
        tokens.append(expression[-1])

    return tokens



def parse(expression: str, tokens: list = None):
    if not tokens:
        tokens = lex(expression)
    list_exp = []
    self_tokens = []
    # Find the outermost parentheses

    opening = []
    closing = []
    # Keep track of where the parentheses expression starts
    opening_idx = -1

    for i, token in enumerate(tokens):
        if is_opening(token):
            if len(opening) == 0:
                opening_idx = i
            opening.append(token)
            continue

        elif is_closing(token):
            if tokens[i-1] == '^':
                list_exp.append('^')
            if len(opening) > 1:
                if opening[-1] == '(' and token == ')':
                    opening.pop()
                if opening[-1] == '[' and token == ']':
                    opening.pop()

                if opening[-1] == '{' and token == '}':
                    opening.pop()
            else:
                list_exp.append(parse(expression, tokens[opening_idx+1:i])[0])
                self_tokens.append("FILL")
                opening.pop()
            continue
        elif not opening:
            self_tokens.append(token)

    exp_iter = iter(list_exp)
    for i, token in enumerate(self_tokens):
        if token == "FILL":
            self_tokens[i] = next(exp_iter)

    while '^' in self_tokens:
        # Evaluate the exponents
        for i, token in enumerate(self_tokens):
            if token == '^':
                rep = (float(self_tokens[i-1]**float(self_tokens[i+1])))
                del self_tokens[i - 1:i + 2]
                self_tokens.insert(i-1, rep)

    # Multiplication and Division
    while '*' in self_tokens or '/' in self_tokens:
        for i, token in enumerate(self_tokens):
            if token == '*':
                rep = float(self_tokens[i-1]*float(self_tokens[i+1]))
                del self_tokens[i - 1:i + 2]
                self_tokens.insert(i-1, rep)
            elif token == '/':
                rep = float(self_tokens[i-1]/float(self_tokens[i+1]))
                del self_tokens[i - 1:i + 2]
                self_tokens.insert(i-1, rep)

    while len(self_tokens) > 1:
        # Addition and Subtraction
        for i, token in enumerate(self_tokens):
            if token == '+':
                rep = float(self_tokens[i-1]+float(self_tokens[i+1]))
                del self_tokens[i - 1:i + 2]
                self_tokens.insert(i-1, rep)
            elif token == '-':
                rep = float(self_tokens[i-1]-float(self_tokens[i+1]))
                del self_tokens[i - 1:i + 2]
                self_tokens.insert(i-1, rep)
    return self_tokens
