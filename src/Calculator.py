import tkinter as tk
from tkinter import ttk
from Parser import parse

expression = ""
result = ""


def press(num):
    global expression
    expression = expression + str(num)
    display_exp.set(expression)


def equals():
    global expression, result
    total = parse(expression)
    expression = str(total[0]) + " "
    display_exp.set(expression)

def clear():
    global expression, result
    expression = ""
    result = ""
    display_exp.set("")


def main_to_graphing():
    main.pack_forget()
    graphing.pack()



if __name__ == "__main__":
    # Set up root window
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x500")

    main = tk.Frame(root)
    graphing = tk.Frame(root)

    # Set up display
    display_exp = tk.StringVar()
    display = tk.Entry(main, textvariable=display_exp)
    display.grid(columnspan=6)

    
    # Set up buttons for main frame
    button_1 = tk.Button(main, text="1", command=lambda: press(1), width=4, height=2)
    button_1.grid(row=1, column=0)
    button_2 = tk.Button(main, text="2", command=lambda: press(2), width=4, height=2)
    button_2.grid(row=1, column=1)
    button_3 = tk.Button(main, text="3", command=lambda: press(3), width=4, height=2)
    button_3.grid(row=1, column=2)
    button_4 = tk.Button(main, text="4", command=lambda: press(4), width=4, height=2)
    button_4.grid(row=2, column=0)
    button_5 = tk.Button(main, text="5", command=lambda: press(5), width=4, height=2)
    button_5.grid(row=2, column=1)
    button_6 = tk.Button(main, text="6", command=lambda: press(6), width=4, height=2)
    button_6.grid(row=2, column=2)
    button_7 = tk.Button(main, text="7", command=lambda: press(7), width=4, height=2)
    button_7.grid(row=3, column=0)
    button_8 = tk.Button(main, text="8", command=lambda: press(8), width=4, height=2)
    button_8.grid(row=3, column=1)
    button_9 = tk.Button(main, text="9", command=lambda: press(9), width=4, height=2)
    button_9.grid(row=3, column=2)
    button_0 = tk.Button(main, text="0", command=lambda: press(0), width=4, height=2)
    button_0.grid(row=4, column=1)
    button_add = tk.Button(main, text="+", command=lambda: press("+"), width=4, height=2)
    button_add.grid(row=1, column=3)
    button_sub = tk.Button(main, text="-", command=lambda: press("-"), width=4, height=2)
    button_sub.grid(row=2, column=3)
    button_mul = tk.Button(main, text="*", command=lambda: press("*"), width=4, height=2)
    button_mul.grid(row=3, column=3)

    button_div = tk.Button(main, text="/", command=lambda: press("/"), width=4, height=2)
    button_div.grid(row=4, column=3)
    button_equal = tk.Button(main, text="=", command=lambda: equals(), width=4, height=2)
    button_equal.grid(row=4, column=2)
    button_clear = tk.Button(main, text="Clear", command=lambda: clear(), width=4, height=2)
    button_clear.grid(row=4, column=0)

    button_decimal = tk.Button(main, text=".", command=lambda: press("."), width=4, height=2)
    button_decimal.grid(row=5, column=0)

    button_graphing = tk.Button(main, text="Graphing", command=lambda: main_to_graphing(), width=4, height=2)
    button_graphing.grid(row=5, column=1)


    # Set up buttons for graphing frame
    polynomial_container = tk.Frame(graphing)
    polynomial_container.grid(columnspan=2)

    function = tk.Label(graphing, text="f( ")
    function.grid(row=0, column=0)

    symbol = tk.StringVar()
    symbol_box = tk.Entry(graphing, textvariable=symbol, width=1)
    symbol_box.grid(row=0, column=1, sticky="W")

    function_cont = tk.Label(graphing, text=") = ")
    function_cont.grid(row=0, column=2)

    c3 = tk.StringVar()
    c3_box = tk.Entry(graphing, textvariable=c3, width=4)
    c3_box.grid(row=0, column=3)
    sym3 = tk.Label(graphing, text="x³")
    sym3.grid(row=0, column=4)

    f3t2 = ttk.Combobox(graphing, values=["+", "-"], width=1)
    f3t2.grid(row=0, column=5, padx=5)

    c2 = tk.StringVar()
    c2_box = tk.Entry(graphing, textvariable=c2, width=4)
    c2_box.grid(row=0, column=6)
    sym2 = tk.Label(graphing, text="x²")
    sym2.grid(row=0, column=7)

    f2t1 = ttk.Combobox(graphing, values=["+", "-"], width=1)
    f2t1.grid(row=0, column=8, padx=5)

    c1 = tk.StringVar()
    c1_box = tk.Entry(graphing, textvariable=c1, width=4)
    c1_box.grid(row=0, column=9)
    sym1 = tk.Label(graphing, text="x")
    sym1.grid(row=0, column=10)

    f1t0 = ttk.Combobox(graphing, values=["+", "-"], width=1)
    f1t0.grid(row=0, column=11, padx=5)

    c0 = tk.StringVar()
    c0_box = tk.Entry(graphing, textvariable=c0, width=1)
    c0_box.grid(row=0, column=12)


    def graphing_symbol_change(*args):
        sym3.config(text=symbol.get() + "³")
        sym2.config(text=symbol.get() + "²")
        sym1.config(text=symbol.get())

    #TODO: Add this callback
    symbol.trace("w", graphing_symbol_change)



    main.pack()

    root.mainloop()
