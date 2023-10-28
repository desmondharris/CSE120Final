from Core import *
import logging
class Symbol:
    def __init__(self, variable: str, value: float=0):
        self.variable = variable
        self.value = value


def lex(expression: str):
    tokens = []
    for l in expression:
        if l.isdigit():
            tokens.append(float(l))
        elif is_basic_operand(l):
            tokens.append(l)
        else:
            logging.warning(f"Unknown character '{l}'")
    return tokens


def parse(expression: str):
    tokens = lex(expression)

    return tokens


class Parser:
    def __init__(self):
        pass

    def evaluate(self, expression: str):
        for l in expression:
            if l == ' ':
                pass
            elif l == '+':
                pass
            elif l == '-':
                pass
            elif l == '*':
                pass
            elif l == '/':
                pass
            elif l == '^':
                pass
            elif l == '(':
                pass
            elif l == ')':
                pass
            else:
                pass