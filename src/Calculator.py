import tkinter as tk

from tkinter import ttk
from Parser import parse
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')


# function to convert to superscript taken from https://www.geeksforgeeks.org/python-convert-string-to-superscript/
# NOT written by students
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


class Calculator:
    def __init__(self):
        self.MAIN_KEY_HEIGHT = 3
        self.MAIN_KEY_WIDTH = 6
        self.GRAPHING_KEY_HEIGHT = 2
        self.GRAPHING_KEY_WIDTH = 4
        self.MAIN_ENTERING_EXPNT = False

        # Dummy values for later
        self.graphing_dict = {
            "c3": 0.0,
            "c2": 0.0,
            "c1": 0.0,
            "c0": 0.0,
            "f3t2": "+",
            "f2t1": "+",
            "f1t0": "+"
        }

        self.expression = ""
        self.result = ""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.main = tk.Frame(self.root)
        self.graphing = tk.Frame(self.root)

        # Set up display
        self.display_exp = tk.StringVar()
        self.display = tk.Entry(self.main, textvariable=self.display_exp, width=self.MAIN_KEY_WIDTH * 6)
        self.display.grid(row=0, column=0, columnspan=4)

        # Set up buttons for main frame
        self.button_1 = tk.Button(self.main, text="1", command=lambda: self.press(1), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_1.grid(row=1, column=0)
        self.button_2 = tk.Button(self.main, text="2", command=lambda: self.press(2), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_2.grid(row=1, column=1)
        self.button_3 = tk.Button(self.main, text="3", command=lambda: self.press(3), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_3.grid(row=1, column=2)
        self.button_4 = tk.Button(self.main, text="4", command=lambda: self.press(4), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_4.grid(row=2, column=0)
        self.button_5 = tk.Button(self.main, text="5", command=lambda: self.press(5), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_5.grid(row=2, column=1)
        self.button_6 = tk.Button(self.main, text="6", command=lambda: self.press(6), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_6.grid(row=2, column=2)
        self.button_7 = tk.Button(self.main, text="7", command=lambda: self.press(7), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_7.grid(row=3, column=0)
        self.button_8 = tk.Button(self.main, text="8", command=lambda: self.press(8), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_8.grid(row=3, column=1)
        self.button_9 = tk.Button(self.main, text="9", command=lambda: self.press(9), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_9.grid(row=3, column=2)
        self.button_0 = tk.Button(self.main, text="0", command=lambda: self.press(0), width=self.MAIN_KEY_WIDTH,
                                  height=self.MAIN_KEY_HEIGHT)
        self.button_0.grid(row=4, column=1)
        self.button_add = tk.Button(self.main, text="+", command=lambda: self.press("+"), width=self.MAIN_KEY_WIDTH,
                                    height=self.MAIN_KEY_HEIGHT)
        self.button_add.grid(row=1, column=3)
        self.button_sub = tk.Button(self.main, text="-", command=lambda: self.press("-"), width=self.MAIN_KEY_WIDTH,
                                    height=self.MAIN_KEY_HEIGHT)
        self.button_sub.grid(row=2, column=3)
        self.button_mul = tk.Button(self.main, text="*", command=lambda: self.press("*"), width=self.MAIN_KEY_WIDTH,
                                    height=self.MAIN_KEY_HEIGHT)
        self.button_mul.grid(row=3, column=3)

        self.button_div = tk.Button(self.main, text="/", command=lambda: self.press("/"), width=self.MAIN_KEY_WIDTH,
                                    height=self.MAIN_KEY_HEIGHT)
        self.button_div.grid(row=4, column=3)
        self.button_equal = tk.Button(self.main, text="=", command=lambda: self.equals(), width=self.MAIN_KEY_WIDTH,
                                      height=self.MAIN_KEY_HEIGHT)
        self.button_equal.grid(row=4, column=2)
        self.button_clear = tk.Button(self.main, text="Clear", command=lambda: self.clear(), width=self.MAIN_KEY_WIDTH,
                                      height=self.MAIN_KEY_HEIGHT)
        self.button_clear.grid(row=4, column=0)

        self.button_decimal = tk.Button(self.main, text=".", command=lambda: self.press("."), width=self.MAIN_KEY_WIDTH,
                                        height=self.MAIN_KEY_HEIGHT)
        self.button_decimal.grid(row=5, column=0)

        self.open_paren = tk.Button(self.main, text="(", command=lambda: self.press("("), width=self.MAIN_KEY_WIDTH,
                                    height=self.MAIN_KEY_HEIGHT)
        self.open_paren.grid(row=5, column=1)

        self.close_paren = tk.Button(self.main, text=")", command=lambda: self.press(")"), width=self.MAIN_KEY_WIDTH,
                                     height=self.MAIN_KEY_HEIGHT)
        self.close_paren.grid(row=5, column=2)

        self.button_graphing = tk.Button(self.main, text="Graphing", command=lambda: self.main_to_graphing(),
                                         width=self.MAIN_KEY_WIDTH, height=self.MAIN_KEY_HEIGHT)
        self.button_graphing.grid(row=5, column=3)

        self.button_exponent = tk.Button(self.main, text="^", command=lambda: self.press_exp(),
                                         width=self.MAIN_KEY_WIDTH, height=self.MAIN_KEY_HEIGHT)
        self.button_exponent.grid(row=6, column=0)

        # GRAPHING
        # Set up buttons for graphing frame
        self.polynomial_container = tk.Frame(self.graphing)
        self.polynomial_container.grid(columnspan=2)

        self.function = tk.Label(self.graphing, text="f( ")
        self.function.grid(row=0, column=0)

        self.symbol = tk.StringVar()
        self.symbol_box = tk.Entry(self.graphing, textvariable=self.symbol, width=1)
        self.symbol_box.grid(row=0, column=1, sticky="W")

        self.function_cont = tk.Label(self.graphing, text=") = ")
        self.function_cont.grid(row=0, column=2)

        self.c3 = tk.StringVar()
        self.c3_box = tk.Entry(self.graphing, textvariable=self.c3, width=4)
        self.c3_box.grid(row=0, column=3)
        self.sym3 = tk.Label(self.graphing, text="x³")
        self.sym3.grid(row=0, column=4)

        self.f3t2 = ttk.Combobox(self.graphing, values=["+", "-"], width=1)
        self.f3t2.grid(row=0, column=5, padx=5)

        self.c2 = tk.StringVar()
        self.c2_box = tk.Entry(self.graphing, textvariable=self.c2, width=4)
        self.c2_box.grid(row=0, column=6)
        self.sym2 = tk.Label(self.graphing, text="x²")
        self.sym2.grid(row=0, column=7)

        self.f2t1 = ttk.Combobox(self.graphing, values=["+", "-"], width=1)
        self.f2t1.grid(row=0, column=8, padx=5)

        self.c1 = tk.StringVar()
        self.c1_box = tk.Entry(self.graphing, textvariable=self.c1, width=4)
        self.c1_box.grid(row=0, column=9)
        self.sym1 = tk.Label(self.graphing, text="x")
        self.sym1.grid(row=0, column=10)

        self.f1t0 = ttk.Combobox(self.graphing, values=["+", "-"], width=1)
        self.f1t0.grid(row=0, column=11, padx=5)

        self.c0 = tk.StringVar()
        self.c0_box = tk.Entry(self.graphing, textvariable=self.c0, width=1)
        self.c0_box.grid(row=0, column=12)

        # Trace certain values to trigger callback functions when changed
        self.symbol.trace("w", self.graphing_symbol_change)
        self.c3.trace("w", self.graphing_fctn_change)

    def press(self, num):
        self.expression = self.expression + str(num)
        if self.MAIN_ENTERING_EXPNT:
            self.display_exp.set(self.display_exp.get() + get_super(str(num)))
        else:
            self.display_exp.set(self.display_exp.get() + str(num))

    def press_exp(self):
        if self.MAIN_ENTERING_EXPNT:
            self.display_exp.set(self.display_exp.get() + get_super(')'))
            self.expression = self.expression + ')'
            self.MAIN_ENTERING_EXPNT = False
        else:
            self.display_exp.set(self.display_exp.get() + get_super('('))
            self.expression = self.expression + '^' + '('
            self.MAIN_ENTERING_EXPNT = True

    def equals(self):
        result = parse(self.expression)[0]
        if result % 1 == 0:
            result = int(result)
        expression = str(result) + " "
        self.display_exp.set(expression)

    def clear(self):
        self.expression = ""
        self.display_exp.set(self.expression)

    def main_to_graphing(self):
        self.main.pack_forget()
        self.graphing.pack()

    def graphing_symbol_change(self, *args):
        self.sym3.config(text=self.symbol.get() + "³")
        self.sym2.config(text=self.symbol.get() + "²")
        self.sym1.config(text=self.symbol.get())

    def graphing_fctn_change(self, *args):
        self.graphing_dict["c3"] = float(self.c3.get())
        self.graphing_dict["c2"] = float(self.c2.get())
        self.graphing_dict["c1"] = float(self.c1.get())
        self.graphing_dict["c0"] = float(self.c0.get())
        self.graphing_dict["f3t2"] = self.f3t2.get()
        self.graphing_dict["f2t1"] = self.f2t1.get()
        self.graphing_dict["f1t0"] = self.f1t0.get()

    def c3_change(self, *args):
        pass

    def start(self):
        self.symbol.set("x")
        self.main.pack(fill=tk.BOTH, expand=True)
        self.root.mainloop()

    def latex_graph(self):
        # self.graphing_ltx = expression
        pass


if __name__ == "__main__":
    calc = Calculator()
    calc.start()

