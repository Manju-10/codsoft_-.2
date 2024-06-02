import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Create display
        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '='
        ]
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, width=5, height=2,
                                font=('Arial', 14), command=lambda x=button_text: self.add_to_display(x))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Create clear button
        clear_button = tk.Button(master, text='C', width=5, height=2,
                                  font=('Arial', 14), command=self.clear_display)
        clear_button.grid(row=5, column=0, padx=5, pady=5)

    def add_to_display(self, value):
        if value == '=':
            try:
                result = str(eval(self.display.get()))
                self.clear_display()
                self.display.insert(0, result)
            except:
                self.clear_display()
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, value)

    def clear_display(self):
        self.display.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
